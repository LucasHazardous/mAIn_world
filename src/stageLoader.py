from entity.player import Player
from entity.enemy.shootingEnemy import ShootingEnemy
from entity.enemy.walkingEnemy import WalkingEnemy
from entity.emp import Emp
from entity.enemy.boss import Boss
from entity.enemy.guardian import Guardian
from config import colorsConfig, gameSettings

import pygame
from pygame.locals import DOUBLEBUF, HWSURFACE

SCREEN_WIDTH = gameSettings["SCREEN_WIDTH"]
SCREEN_HEIGHT = gameSettings["SCREEN_HEIGHT"]
FPS = gameSettings["FPS"]
DEPTH = gameSettings["DEPTH"]
SPRITESHEET_PATH = gameSettings["SPRITESHEET_PATH"]

class StageLoader():
    def __init__(self):
        pygame.display.set_caption("mAIn_world")
        
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        
        flags = DOUBLEBUF | HWSURFACE
        
        self.__clock = pygame.time.Clock()
        
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, DEPTH)

        self.__playerSpritesheet = pygame.image.load(SPRITESHEET_PATH + "player.png").convert_alpha()
        self.__shootingEnemySpritesheet = pygame.image.load(SPRITESHEET_PATH + "shootingEnemy.png").convert_alpha()
        self.__projectile = pygame.image.load(SPRITESHEET_PATH + "projectile.png").convert_alpha()
        self.__empSpritesheet = pygame.image.load(SPRITESHEET_PATH + "emp.png").convert_alpha()
        self.__bossSpritesheet = pygame.image.load(SPRITESHEET_PATH + "boss.png").convert_alpha()
        self.__walkingEnemySpritesheet = pygame.image.load(SPRITESHEET_PATH + "walkingEnemy.png").convert_alpha()
        self.__guardianSpritesheet = pygame.image.load(SPRITESHEET_PATH + "guardian.png").convert_alpha()
        
        self.__emp = Emp(0, 0, self.__empSpritesheet)

    def __playAudio(self, audioPath, loop=-1):
        pygame.mixer.music.load(audioPath)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loop, 0.0, 5000)


    def __drawBackground(self, background):
        scaledBackground = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__screen.blit(scaledBackground, (0,0))
        
        
    def __drawHealthBar(self, entity):
        pygame.draw.rect(self.__screen, colorsConfig["HEALTHBAR_BG"], (entity.body.left - 5, entity.body.top - 55, entity.body.width+10, 40))
        ratio = entity.health / entity.baseHealth
        pygame.draw.rect(self.__screen, colorsConfig["HEALTHBAR_MAIN"], (entity.body.left, entity.body.top-50, entity.body.width * ratio, 30))


    def playCutscene(self, category, audio, background):
        self.__playAudio(audio, 1)
        
        img = pygame.image.load(background).convert()
        self.__drawBackground(img)
        pygame.display.update()
        
        while pygame.mixer.music.get_busy():
            self.__clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()


    def loadNormalStage(self, category, background, audio, playerPos, shootingEnemiesPos=[], walkingEnemiesPos=[], bossPos=None, guardianPos=None):
        convertedBackground = pygame.image.load(background).convert()
        
        player = Player(playerPos[0], playerPos[1], self.__playerSpritesheet, self.__emp)
        
        enemies = []
        
        for enemyPos in shootingEnemiesPos:
            enemies.append(ShootingEnemy(enemyPos[0], enemyPos[1], self.__shootingEnemySpritesheet, self.__projectile))
            
        for enemyPos in walkingEnemiesPos:
            enemies.append(WalkingEnemy(enemyPos[0], enemyPos[1], self.__walkingEnemySpritesheet))
        
        if(bossPos != None):
            enemies.append(Boss(bossPos[0], bossPos[1], self.__bossSpritesheet))
            
        if(guardianPos != None):
            enemies.append(Guardian(guardianPos[0], guardianPos[1], self.__guardianSpritesheet))
        
        if(audio != ""): self.__playAudio(audio)
        self.__emp.finished = False
        
        repeatThisStage = False
        
        while 1:
            self.__clock.tick(FPS)
            self.__drawBackground(convertedBackground)


            if(player.alive):
                player.move(SCREEN_WIDTH, SCREEN_HEIGHT, self.__screen, enemies)
                if len(enemies) == 0 and player.readyForNextStage: break
            elif(pygame.key.get_pressed()[pygame.K_r]):
                repeatThisStage = True
                break
            
            self.__drawHealthBar(player)
            player.draw(self.__screen)
            player.updateAnimation(self.__screen, enemies)
        
        
            for enemy in enemies:
                self.__drawHealthBar(enemy)
                enemy.draw(self.__screen)
                enemy.updateAnimation(self.__screen, player)
                if(not enemy.alive): enemies.remove(enemy)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                
            pygame.display.update()
            
        if(repeatThisStage): self.loadNormalStage(category, background, audio, playerPos, shootingEnemiesPos, walkingEnemiesPos, bossPos, guardianPos)
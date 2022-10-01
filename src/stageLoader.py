from entity.player import Player
from entity.enemy import Enemy
from entity.emp import Emp
from entity.boss import Boss
from config import colors_config

import pygame
from pygame.locals import DOUBLEBUF, HWSURFACE

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60
DEPTH = 24

SPRITESHEET_PATH = "./assets/images/entities/"

class StageLoader():
    def __init__(self):
        pygame.display.set_caption("mAIn_world")
        
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        
        self.flags = DOUBLEBUF | HWSURFACE
        
        self.__clock = pygame.time.Clock()
        
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), self.flags, DEPTH)

        self.__player_spritesheet = pygame.image.load(SPRITESHEET_PATH + "player.png").convert_alpha()
        self.__enemy_spritesheet = pygame.image.load(SPRITESHEET_PATH + "enemy.png").convert_alpha()
        self.__projectile = pygame.image.load(SPRITESHEET_PATH + "projectile.png").convert_alpha()
        self.__emp_spritesheet = pygame.image.load(SPRITESHEET_PATH + "emp.png").convert_alpha()
        
        self.__emp = Emp(0, 0, self.__emp_spritesheet)

    def __playMusic(self, musicPath):
        pygame.mixer.music.load(musicPath)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)


    def __drawBackground(self, bg_image):
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__screen.blit(scaled_bg, (0,0))
        
        
    def __drawHealthBar(self, health, x, y, length, base_health):
        pygame.draw.rect(self.__screen, colors_config["HEALTHBAR_BG"], (x-5, y-5, length+10, 40))
        ratio = health / base_health
        pygame.draw.rect(self.__screen, colors_config["HEALTHBAR_MAIN"], (x, y, length * ratio, 30))


    def playCutscene(self, audioPath, imagePath):
        pygame.mixer.music.load(audioPath)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(1, 0.0, 5000)
        
        img = pygame.image.load(imagePath).convert()
        self.__drawBackground(img)
        pygame.display.update()
        
        while pygame.mixer.music.get_busy():
            self.__clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()


    def playInteractiveStage(self, bgImagePath, musicPath, playerPos, enemiesPos):
        bg_image = pygame.image.load(bgImagePath).convert_alpha()
        player = Player(playerPos[0], playerPos[1], self.__player_spritesheet, self.__emp)
        enemies = [Enemy(enemyPos[0], enemyPos[1], self.__enemy_spritesheet, self.__projectile) for enemyPos in enemiesPos]
        if(musicPath != ""): self.__playMusic(musicPath)
        self.__emp.finished = False
        
        while 1:
            self.__clock.tick(FPS)
            self.__drawBackground(bg_image)


            if(player.alive):
                player.move(SCREEN_WIDTH, SCREEN_HEIGHT, self.__screen, enemies)
                if len(enemies) == 0 and player.readyForNextStage: break
            elif(pygame.key.get_pressed()[pygame.K_r]):
                self.playInteractiveStage(bgImagePath, musicPath, playerPos, enemiesPos)
                break
            
            self.__drawHealthBar(player.health, player.body.left, player.body.top-50, player.body.width, player.base_health)
            player.draw(self.__screen)
            player.updateAnimation(self.__screen, enemies)
        
        
            for enemy in enemies:
                self.__drawHealthBar(enemy.health, enemy.body.left, enemy.body.top-50, enemy.body.width, enemy.base_health)
                enemy.draw(self.__screen)
                enemy.updateAnimation(self.__screen, player)
                if(not enemy.alive): enemies.remove(enemy)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                
            pygame.display.update()
            

    def playBossFight(self, bgImagePath, musicPath, playerPos, bossPos):
        boss_spritesheet = pygame.image.load(SPRITESHEET_PATH + "boss.png").convert_alpha()
        boss = Boss(bossPos[0], bossPos[1], boss_spritesheet)
        enemies = [boss]
        
        bg_image = pygame.image.load(bgImagePath).convert_alpha()
        player = Player(playerPos[0], playerPos[1], self.__player_spritesheet, self.__emp)
        
        if(musicPath != ""): self.__playMusic(musicPath)
        self.__emp.finished = False
        
        while 1:
            self.__clock.tick(FPS)
            self.__drawBackground(bg_image)


            if(player.alive):
                player.move(SCREEN_WIDTH, SCREEN_HEIGHT, self.__screen, enemies)
                if player.readyForNextStage and not boss.alive: break
            elif(pygame.key.get_pressed()[pygame.K_r]):
                self.playBossFight(bgImagePath, musicPath, playerPos, bossPos)
                break

            self.__drawHealthBar(player.health, player.body.left, player.body.top-50, player.body.width, player.base_health)
            player.draw(self.__screen)
            player.updateAnimation(self.__screen, enemies)
            
            if(boss.alive): boss.updateAnimation(self.__screen, player)
            boss.draw(self.__screen)
            self.__drawHealthBar(boss.health, boss.body.left, boss.body.top-50, boss.body.width, boss.base_health)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                
            pygame.display.update()
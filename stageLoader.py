from entity.player import Player
from entity.enemy import Enemy
import pygame
from config import colors_config

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60
DEPTH = 24

class StageLoader():
    def __init__(self):
        pygame.display.set_caption("")
        
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        
        from pygame.locals import DOUBLEBUF, HWSURFACE
        self.flags = DOUBLEBUF | HWSURFACE
        
        self.__clock = pygame.time.Clock()
        
        self.__loadScreen()

        self.__player_spritesheet = pygame.image.load("./assets/images/player.png").convert_alpha()
        self.__enemy_spritesheet = pygame.image.load("./assets/images/enemy.png").convert_alpha()
        self.__projectile = pygame.image.load("./assets/images/projectile.png").convert_alpha()
        
        
    def __loadScreen(self):
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), self.flags, DEPTH)
      

    def __playMusic(self, musicPath):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(musicPath)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)


    def __drawBackground(self, bg_image):
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__screen.blit(scaled_bg, (0,0))
        
        
    def __drawHealthBar(self, health, x, y, length):
        pygame.draw.rect(self.__screen, colors_config["HEALTHBAR_BG"], (x-5, y-5, length+10, 40))
        ratio = health / 100
        pygame.draw.rect(self.__screen, colors_config["HEALTHBAR_MAIN"], (x, y, length * ratio, 30))


    def playVideo(self, videoPath):
        import moviepy.editor
        video = moviepy.editor.VideoFileClip(videoPath, verbose=False)
        video.preview()
        video.close()


    def playInteractiveStage(self, bgImagePath, musicPath, playerPos, enemiesPos):
        self.__loadScreen()
        
        bg_image = pygame.image.load(bgImagePath).convert_alpha()
        player = Player(playerPos[0], playerPos[1], self.__player_spritesheet)
        enemies = [Enemy(enemyPos[0], enemyPos[1], self.__enemy_spritesheet, self.__projectile) for enemyPos in enemiesPos]
        self.__playMusic(musicPath)
        
        while 1:
            self.__clock.tick(FPS)
            self.__drawBackground(bg_image)

            player.move(SCREEN_WIDTH, SCREEN_HEIGHT, self.__screen, enemies)
            
            self.__drawHealthBar(player.health, player.body.left, player.body.top-50, player.body.width)
            player.draw(self.__screen)
            
            player.updateAnimation(self.__screen, enemies)
            
            for enemy in enemies:
                self.__drawHealthBar(enemy.health, enemy.body.left, enemy.body.top-50, enemy.body.width)
                enemy.draw(self.__screen)
                enemy.updateAnimation(self.__screen, player)
                if(enemy.toRemove): enemies.remove(enemy)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                
            pygame.display.update()
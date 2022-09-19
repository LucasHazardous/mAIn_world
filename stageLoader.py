from entity import Player, Enemy
import pygame

YELLOW = (255, 255, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60
DEPTH = 24

class StageLoader():
    def __init__(self):
        pygame.display.set_caption("")
        
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        
        from pygame.locals import DOUBLEBUF, HWSURFACE
        flags = DOUBLEBUF | HWSURFACE
        
        self.clock = pygame.time.Clock()
    
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, DEPTH)

        self.player_spritesheet = pygame.image.load("./assets/images/player.png").convert_alpha()
      

    def playMusic(self, musicPath):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(musicPath)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)


    def drawBackground(self, bg_image):
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(scaled_bg, (0,0))
        
        
    def drawHealthBar(self, health, x, y, length):
        pygame.draw.rect(self.screen, (0,0,0), (x-5, y-5, length+10, 40))
        ratio = health / 100
        pygame.draw.rect(self.screen, YELLOW, (x, y, length * ratio, 30))


    def playVideo(self, videoPath):
        import moviepy.editor
        video = moviepy.editor.VideoFileClip(videoPath, verbose=False)
        video.preview()
        video.close()


    def loadStage(self, bgImagePath, musicPath, playerPos, enemiesPos):
        bg_image = pygame.image.load(bgImagePath).convert_alpha()
        player = Player(playerPos[0], playerPos[1], self.player_spritesheet)
        enemies = [Enemy(enemyPos[0], enemyPos[1]) for enemyPos in enemiesPos]
        self.playMusic(musicPath)
        
        while 1:
            self.clock.tick(FPS)
            self.drawBackground(bg_image)

            player.move(SCREEN_WIDTH, SCREEN_HEIGHT, self.screen, enemies)
            
            self.drawHealthBar(player.health, player.body.left, player.body.top-50, player.body.width)
            player.draw(self.screen)
            
            player.updateAnimation(self.screen, enemies)
            
            for enemy in enemies:
                self.drawHealthBar(enemy.health, enemy.body.left, enemy.body.top-50, enemy.body.width)
                enemy.draw(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            pygame.display.update()
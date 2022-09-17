import pygame
from entity import Player, Enemy
from pygame import mixer
import moviepy.editor

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

YELLOW = (255, 255, 0)

pygame.display.set_caption("")

def setGameMode():
    global clock, screen, bg_image, player_spritesheet
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    bg_image = pygame.image.load("./assets/images/first.png").convert_alpha()
    player_spritesheet = pygame.image.load("./assets/images/player.png").convert_alpha()


def playMusic():
    pygame.mixer.music.load("./assets/audio/music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)


def drawBackground():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))
    
    
def drawHealthBar(health, x, y, length):
    pygame.draw.rect(screen, (0,0,0), (x-5, y-5, length+10, 40))
    ratio = health / 100
    pygame.draw.rect(screen, YELLOW, (x, y, length * ratio, 30))


def playVideo(videoPath):
    video = moviepy.editor.VideoFileClip(videoPath, verbose=False)
    video.preview()
    video.close()
    
setGameMode()

player = Player(200, 380, False, player_spritesheet)
enemies = [Enemy(500, 380)]

run = True
while run:
    clock.tick(FPS)
    drawBackground()

    player.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, enemies)
    
    drawHealthBar(player.health, player.body.left, player.body.top-50, player.body.width)
    player.draw(screen)
    
    player.updateAnimation(screen, enemies)
    
    for enemy in enemies:
        drawHealthBar(enemy.health, enemy.body.left, enemy.body.top-50, enemy.body.width)
        enemy.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.quit()
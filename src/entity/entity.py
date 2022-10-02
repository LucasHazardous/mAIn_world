from time import time
import pygame

class Entity():
    def __init__(self, x, y, entity_spritesheet, entity_config):
        self.baseHealth = entity_config["BASE_HEALTH"]
        self.health = self.baseHealth
        
        self.alive = True
        self.flip = True
        self.attacking = False
        
        self.lastAnimationUpdateTime = pygame.time.get_ticks()
        self.animationCooldown = entity_config["ANIMATION_COOLDOWN"]
        self.sizeX = entity_config["SIZE_X"]
        self.sizeY = entity_config["SIZE_Y"]
        self.offset = entity_config["OFFSET"]
        
        self.body = pygame.Rect((x, y, entity_config["HITBOX_WIDTH"], entity_config["HITBOX_HEIGHT"]))
        self.imageScale = entity_config["SCALE"]
        self.action = 0
        self.frameIndex = 0
        
        self.animationList = self.loadImages(entity_spritesheet, entity_config["ANIMATION_STEPS"])
    
        self.image = self.animationList[self.action][self.frameIndex]
    
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.body.x-self.offset[0]*self.imageScale, self.body.y-self.offset[1]*self.imageScale))
        
        
    def loadImages(self, sprite_sheet: pygame.Surface, animation_steps):
        animationList = []
        for j, animation in enumerate(animation_steps):
            temporaryAnimationList = []
            for i in range(animation):
                temp_img = sprite_sheet.subsurface(i*self.sizeX, j*self.sizeY, self.sizeX, self.sizeY)
                temporaryAnimationList.append(pygame.transform.scale(temp_img, (self.sizeX*self.imageScale, self.sizeY*self.imageScale)))
            animationList.append(temporaryAnimationList)
        return animationList
    
    
    def updateAction(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frameIndex = 0
            self.lastAnimationUpdateTime = pygame.time.get_ticks()
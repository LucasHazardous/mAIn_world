from time import time
import pygame

class Entity():
    def __init__(self, x, y, entitySpritesheet, entityConfig):
        self.baseHealth = entityConfig["BASE_HEALTH"]
        self.health = self.baseHealth
        
        self.alive = True
        self.flip = True
        self.attacking = False
        
        self.lastAnimationUpdateTime = pygame.time.get_ticks()
        self.animationCooldown = entityConfig["ANIMATION_COOLDOWN"]
        self.sizeX = entityConfig["SIZE_X"]
        self.sizeY = entityConfig["SIZE_Y"]
        self.offset = entityConfig["OFFSET"]
        
        self.body = pygame.Rect((x, y, entityConfig["HITBOX_WIDTH"], entityConfig["HITBOX_HEIGHT"]))
        self.imageScale = entityConfig["SCALE"]
        self.action = 0
        self.frameIndex = 0
        
        self.animationList = self.loadImages(entitySpritesheet, entityConfig["ANIMATION_STEPS"])
    
        self.image = self.animationList[self.action][self.frameIndex]
    
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.body.x-self.offset[0]*self.imageScale, self.body.y-self.offset[1]*self.imageScale))
        
        
    def loadImages(self, spritesheet, animationSeps):
        animationList = []
        for j, animation in enumerate(animationSeps):
            temporaryAnimationList = []
            for i in range(animation):
                tempImg = spritesheet.subsurface(i*self.sizeX, j*self.sizeY, self.sizeX, self.sizeY)
                temporaryAnimationList.append(pygame.transform.scale(tempImg, (self.sizeX*self.imageScale, self.sizeY*self.imageScale)))
            animationList.append(temporaryAnimationList)
        return animationList
    
    
    def updateAction(self, newAction):
        if newAction != self.action:
            self.action = newAction
            self.frameIndex = 0
            self.lastAnimationUpdateTime = pygame.time.get_ticks()
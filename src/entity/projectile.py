import pygame
from time import time
from config import projectileConfig
from entity.entity import Entity

class Projectile(Entity):
    def __init__(self, x, y, projectileSpritesheet):
        super().__init__(x, y, projectileSpritesheet, projectileConfig)
        self.updateAction(projectileConfig["ANIM_FLY"])
        
        
    def updateAnimation(self, surface, target):
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            
        self.body.x -= projectileConfig["SPEED"]
        self.attackTarget(target)
        
    def goToPosition(self, x, y):
        self.body.x = x
        self.body.y = y
        
    def attackTarget(self, target):
        if self.body.colliderect(target.body):
            self.body.y = -projectileConfig["HITBOX_HEIGHT"]
            target.health -= projectileConfig["DAMAGE"]
            target.hit = True
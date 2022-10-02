import pygame
from time import time
from config import projectile_config
from entity.entity import Entity

class Projectile(Entity):
    def __init__(self, x, y, projectile_spritesheet):
        super().__init__(x, y, projectile_spritesheet, projectile_config)
        self.updateAction(projectile_config["ANIM_FLY"])
        
        
    def updateAnimation(self, surface, target):
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            
        self.body.x -= projectile_config["SPEED"]
        self.attackTarget(target)
        
    def goToPosition(self, x, y):
        self.body.x = x
        self.body.y = y
        
    def attackTarget(self, target):
        if self.body.colliderect(target.body):
            self.body.y = -projectile_config["HITBOX_HEIGHT"]
            target.health -= projectile_config["DAMAGE"]
            target.hit = True
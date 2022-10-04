import pygame
from time import time
from config import enemyConfig
from entity.entity import Entity
from entity.projectile import Projectile

class Enemy(Entity):
    def __init__(self, x, y, enemySpritesheet, projectileSpritesheet):
        super().__init__(x, y, enemySpritesheet, enemyConfig)
        self.projectile = Projectile(self.body.centerx, self.body.centery, projectileSpritesheet)
        
    def updateAnimation(self, surface, target):
        if self.health <= 0:
            self.health = 0
            self._updateAction(enemyConfig["ANIM_DEATH"])
        else: self._updateAction(enemyConfig["ANIM_ATTACK"])
        
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            if self.action == enemyConfig["ANIM_ATTACK"]:
                self.attacking = False
            elif self.action == enemyConfig["ANIM_DEATH"]:
                self.alive = False
                
        if (self.action == enemyConfig["ANIM_ATTACK"] and self.frameIndex >= enemyConfig["ANIMATION_STEPS"][enemyConfig["ANIM_ATTACK"]]-1):
            self.projectile.goToPosition(self.body.centerx, self.body.centery)
            
        self.projectile.updateAnimation(surface, target)
        self.projectile.draw(surface)
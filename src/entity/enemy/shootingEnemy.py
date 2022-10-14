import pygame
from time import time
from config import shootingEnemyConfig
from entity.entity import Entity
from entity.enemy.projectile import Projectile

class ShootingEnemy(Entity):
    def __init__(self, x, y, enemySpritesheet, projectileSpritesheet):
        super().__init__(x, y, enemySpritesheet, shootingEnemyConfig)
        self.projectile = Projectile(self.body.centerx, self.body.centery, projectileSpritesheet)
        
    def updateAnimation(self, surface, target):
        if self.health <= 0:
            self.health = 0
            self._updateAction(shootingEnemyConfig["ANIM_DEATH"])
        else: self._updateAction(shootingEnemyConfig["ANIM_ATTACK"])
        
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            if self.action == shootingEnemyConfig["ANIM_ATTACK"]:
                self.attacking = False
            elif self.action == shootingEnemyConfig["ANIM_DEATH"]:
                self.alive = False
                
        if (self.action == shootingEnemyConfig["ANIM_ATTACK"] and self.frameIndex >= shootingEnemyConfig["ANIMATION_STEPS"][shootingEnemyConfig["ANIM_ATTACK"]]-1):
            self.projectile.goToPosition(self.body.centerx, self.body.centery)
            
        self.projectile.updateAnimation(surface, target)
        self.projectile.draw(surface)
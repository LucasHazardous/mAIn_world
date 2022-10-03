import pygame
from time import time
from config import enemy_config
from entity.entity import Entity
from entity.projectile import Projectile

class Enemy(Entity):
    def __init__(self, x, y, enemy_spritesheet, projectile_spritesheet):
        super().__init__(x, y, enemy_spritesheet, enemy_config)
        self.projectile = Projectile(self.body.centerx, self.body.centery, projectile_spritesheet)
        
    def updateAnimation(self, surface, target):
        if self.health <= 0:
            self.health = 0
            self.updateAction(enemy_config["ANIM_DEATH"])
        else: self.updateAction(enemy_config["ANIM_ATTACK"])
        
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            if self.action == enemy_config["ANIM_ATTACK"]:
                self.attacking = False
            elif self.action == enemy_config["ANIM_DEATH"]:
                self.alive = False
                
        if (self.action == enemy_config["ANIM_ATTACK"] and self.frameIndex >= enemy_config["ANIMATION_STEPS"][enemy_config["ANIM_ATTACK"]]-1):
            self.projectile.goToPosition(self.body.centerx, self.body.centery)
            
        self.projectile.updateAnimation(surface, target)
        self.projectile.draw(surface)
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
        self.image = self.animation_list[self.action][self.frame_index]
        
        if current - self.last_animation_update_time > self.animation_cooldown:
            self.frame_index += 1
            self.last_animation_update_time = current
            
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            if self.action == enemy_config["ANIM_ATTACK"]:
                self.attacking = False
                self.attack_stages = set()
            elif self.action == enemy_config["ANIM_DEATH"]:
                self.alive = False
                
        if (self.action == enemy_config["ANIM_ATTACK"] and self.frame_index >= enemy_config["ANIMATION_STEPS"][enemy_config["ANIM_ATTACK"]]-1):
            self.projectile.goToPosition(self.body.centerx, self.body.centery)
            
        self.projectile.updateAnimation(surface, target)
        self.projectile.draw(surface)
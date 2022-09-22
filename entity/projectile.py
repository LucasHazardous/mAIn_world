import pygame
from time import time
from config import projectile_config
from entity.entity import Entity

class Projectile(Entity):
    def __init__(self, x, y, projectile_spritesheet):
        Entity.__init__(self, x, y, projectile_spritesheet, projectile_config)
        self.updateAction(projectile_config["ANIM_FLY"])
        
        
    def updateAnimation(self, surface, target):
        current = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.frame_index]
        
        if current - self.last_animation_update_time > self.animation_cooldown:
            self.frame_index += 1
            self.last_animation_update_time = current
            
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            
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
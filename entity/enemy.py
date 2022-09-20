import pygame
from time import time
from config import enemy_config
from entity.entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, enemy_spritesheet):
        Entity.__init__(self, x, y, enemy_spritesheet, enemy_config)
        
        
    def updateAnimation(self, surface, enemies):
        if self.health <= 0:
            self.health = 0
            self.alive = False
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
                
        if self.action == enemy_config["ANIM_ATTACK"] and self.frame_index % 4 == 0 and self.frame_index not in self.attack_stages:
            self.attack(surface, self.getClosetEnemy(enemies))
            self.attack_stages.add(self.frame_index)
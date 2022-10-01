import pygame
from time import time
from config import emp_config
from entity.entity import Entity

class Emp(Entity):
    def __init__(self, x, y, emp_spritesheet):
        super().__init__(x, y, emp_spritesheet, emp_config)
        self.updateAction(emp_config["ANIM_BLAST"])
        self.finished = False
        
    def updateAnimation(self):
        current = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.frame_index]
        
        if current - self.last_animation_update_time > self.animation_cooldown:
            self.frame_index += 1
            self.last_animation_update_time = current
            
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            self.finished = True
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
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            self.finished = True
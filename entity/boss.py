import pygame
from time import time
from config import boss_config
from entity.entity import Entity

class Boss(Entity):
    def __init__(self, x, y, boss_spritesheet):
        Entity.__init__(self, x, y, boss_spritesheet, boss_config)
        
    def updateAnimation(self, surface, player):
        attack_range = pygame.Rect(self.body.centerx - self.body.width, self.body.top, self.body.width*2, self.body.height)
        
        if self.health <= 0:
            self.health = 0
            self.updateAction(boss_config["ANIM_DEATH"])
        elif (attack_range.colliderect(player.body)): self.updateAction(boss_config["ANIM_DASH"])
        else: self.updateAction(boss_config["ANIM_RUN"])
        
        current = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.frame_index]
        
        if current - self.last_animation_update_time > self.animation_cooldown:
            self.frame_index += 1
            self.last_animation_update_time = current
            
        if self.action == boss_config["ANIM_DASH"] and self.frame_index == boss_config["ANIM_DASH_ATTACK_FRAME"]:
                if(attack_range.colliderect(player.body)):
                    player.health -= boss_config["DAMAGE"]
                    player.hit = True
                    self.frame_index += 1
            
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            if self.action == boss_config["ANIM_DEATH"]:
                self.alive = True

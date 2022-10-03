import pygame
from time import time
from config import bossConfig
from entity.entity import Entity
from random import randrange

class Boss(Entity):
    def __init__(self, x, y, bossSpritesheet):
        super().__init__(x, y, bossSpritesheet, bossConfig)
        
    def updateAnimation(self, surface, player):
        attackRange = pygame.Rect(self.body.centerx - self.body.width, self.body.top - self.body.height, self.body.width*2, self.body.height * 2)
        
        if self.health <= 0:
            self.health = 0
            self.updateAction(bossConfig["ANIM_DEATH"])
        elif (attackRange.colliderect(player.body)): self.updateAction(bossConfig["ANIM_DASH"])
        else: self.updateAction(bossConfig["ANIM_RUN"])
        
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.action == bossConfig["ANIM_DASH"] and self.frameIndex == bossConfig["ANIM_DASH_ATTACK_FRAME"]:
                if(attackRange.colliderect(player.body)):
                    player.health -= bossConfig["DAMAGE"]
                    player.hit = True
                    self.frameIndex += 1
                    self.body.x = randrange(bossConfig["TELEPORT_RANGE"][0], bossConfig["TELEPORT_RANGE"][1])
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            if self.action == bossConfig["ANIM_DEATH"]:
                self.alive = False

        if(self.action == bossConfig["ANIM_RUN"]): self.moveCloserToPlayer(player)

    def moveCloserToPlayer(self, player):
        if(player.body.centerx > self.body.centerx):
            self.body.x += bossConfig["SPEED"]
            self.flip = False
        elif(player.body.centerx < self.body.centerx):
            self.body.x -= bossConfig["SPEED"]
            self.flip = True
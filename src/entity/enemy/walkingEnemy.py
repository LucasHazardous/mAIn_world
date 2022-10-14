import pygame
from time import time
from config import walkingEnemyConfig
from entity.entity import Entity

class WalkingEnemy(Entity):
    def __init__(self, x, y, enemySpritesheet):
        super().__init__(x, y, enemySpritesheet, walkingEnemyConfig)
        
    def updateAnimation(self, surface, player):
        if self.health <= 0:
            self.health = 0
            self.alive = False
        else: self._updateAction(walkingEnemyConfig["ANIM_WALK"])
        
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            
        self.__moveCloserToPlayer(player)
            
    def __moveCloserToPlayer(self, player):
        if(player.body.centerx > self.body.centerx):
            self.body.x += walkingEnemyConfig["SPEED"]
            self.flip = False
        elif(player.body.centerx < self.body.centerx):
            self.body.x -= walkingEnemyConfig["SPEED"]
            self.flip = True
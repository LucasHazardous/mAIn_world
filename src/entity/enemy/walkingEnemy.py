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
        self.__attackPlayer(surface, player)
            
    def __moveCloserToPlayer(self, player):
        if(player.body.centerx > self.body.centerx):
            self.body.x += walkingEnemyConfig["SPEED"]
            self.flip = False
        elif(player.body.centerx < self.body.centerx):
            self.body.x -= walkingEnemyConfig["SPEED"]
            self.flip = True
            
    def __attackPlayer(self, surface, player):
        attackRange = pygame.Rect(self.body.left if self.flip else self.body.right, self.body.top+40, walkingEnemyConfig["ATTACK_WIDTH"], self.body.height-40)
        pygame.draw.rect(surface, (0,255,0), attackRange)
        
        if(attackRange.colliderect(player.body)):
            player.health -= walkingEnemyConfig["DAMAGE"]
            player.hit = True
            player.body.x += -walkingEnemyConfig["ATTACK_WIDTH"] if self.flip else walkingEnemyConfig["ATTACK_WIDTH"]
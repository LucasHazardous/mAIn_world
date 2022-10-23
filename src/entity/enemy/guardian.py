import pygame
from time import time
from config import guardianConfig
from entity.entity import Entity
from random import randrange


class Guardian(Entity):
    def __init__(self, x, y, guardianSpritesheet):
        super().__init__(x, y, guardianSpritesheet, guardianConfig)
        self.hit = False

    def updateAnimation(self, surface, player):
        attackRange = pygame.Rect((self.body.left if self.flip else self.body.right)-self.body.width,
                                  self.body.top-self.body.height*0.5, self.body.width*2, self.body.height*1.5)

        if self.health <= 0 or not player.alive:
            self.health = 0
            self._updateAction(guardianConfig["ANIM_DEATH"])
        elif (attackRange.colliderect(player.body)):
            self._updateAction(guardianConfig["ANIM_ATTACK"])
        elif self.hit:
            self._updateAction(guardianConfig["ANIM_HIT"])
        else:
            self._updateAction(guardianConfig["ANIM_RUN"])

        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]

        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current

        if self.action == guardianConfig["ANIM_ATTACK"] and self.frameIndex == guardianConfig["ATTACK_FRAME"]:
            if (attackRange.colliderect(player.body)):
                player.health -= guardianConfig["DAMAGE"]
                player.hit = True
                player.body.y -= 100
                self.frameIndex += 1

        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            if self.action == guardianConfig["ANIM_DEATH"]:
                self.alive = False
            elif self.action == guardianConfig["ANIM_HIT"]:
                self.hit = False

        if (self.action == guardianConfig["ANIM_RUN"]):
            self.__moveCloserToPlayer(player)

    def __moveCloserToPlayer(self, player):
        if (player.body.centerx > self.body.centerx):
            self.body.x += guardianConfig["SPEED"]
            self.flip = False
        elif (player.body.centerx < self.body.centerx):
            self.body.x -= guardianConfig["SPEED"]
            self.flip = True

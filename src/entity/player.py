import pygame
from math import inf, sqrt
from typing import List
from time import time
from config import player_config
from entity.entity import Entity


class Player(Entity):
    def __init__(self, x, y, player_spritesheet, emp):
        super().__init__(x, y, player_spritesheet, player_config)
        self.emp = emp
        self.empUsed = False
        
        self.velX = 1
        self.velY = 0
        self.baseSpeed = player_config["BASE_SPEED"]

        self.health = player_config["BASE_HEALTH"]
        
        self.flip = False
        self.running = False
        self.jumping = False
        self.attacking = False
        self.hit = False
        self.alive = True
        
        self.readyForNextStage = False
        
        self.stagesDealingDamage = set()
        
    def move(self, screenWidth: int, screenHeight: int, surface: pygame.Surface, enemies: List):
        self.readyForNextStage = False
        self.changeX = 0
        self.changeY = 0
        self.running = False
        key = pygame.key.get_pressed()
        
        self.jumpIfAllowed(key)
        
        self.performAttackIfAllowed(key, surface, enemies)
        
        self.useEmpIfAvailable(key, surface, enemies)

        self.verticalPlayerMovement(key, player_config["VERTICAL_ACCELERATION_LIMIT"])
        
        self.leftRightBorderLimit(screenWidth)
            
        self.groundLimit(screenHeight)
            
        self.body.x += self.changeX
        self.body.y += self.changeY
        
    
    def useEmpIfAvailable(self, key, screen, enemies):
        if(not self.empUsed and key[pygame.K_s]):
            self.empUsed = True
            self.emp.body.x = self.body.x
            self.emp.body.y = self.body.y
            for enemy in enemies: self.attack(screen, enemy, player_config["EMP_DAMAGE"])
        
        if(not self.emp.finished and self.empUsed):
            self.emp.draw(screen)
            self.emp.updateAnimation()
            self.empUsed = True
        
        
    def groundLimit(self, screenHeight):
        if self.body.bottom + self.changeY > screenHeight - 50:
            self.velY = 0
            self.jumping = False
            self.changeY = screenHeight - 50 - self.body.bottom
        
        
    def updateAnimation(self, surface, enemies):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.updateAction(player_config["ANIM_DEATH"])
        elif self.hit: self.updateAction(player_config["ANIM_HIT"])
        elif self.attacking: self.updateAction(player_config["ANIM_ATTACK"])
        elif self.jumping: self.updateAction(player_config["ANIM_JUMP"])
        elif self.running: self.updateAction(player_config["ANIM_RUN"])
        else: self.updateAction(player_config["ANIM_IDLE"])
        
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            if self.action == player_config["ANIM_ATTACK"]:
                self.attacking = False
            elif self.action == player_config["ANIM_HIT"]:
                self.attacking = False
                self.hit = False
            elif self.alive == False:
                self.frameIndex = len(self.animationList[self.action]) - 1
                
        if self.action == player_config["ANIM_ATTACK"] and self.frameIndex % 4 == 0 and self.frameIndex not in self.stagesDealingDamage:
            if(len(enemies) > 0): self.attack(surface, self.getClosetEnemy(enemies), player_config["DAMAGE"])
            self.stagesDealingDamage.add(self.frameIndex)
            
     
    def verticalPlayerMovement(self, key, limitVelX):
        if key[pygame.K_a]:
            if(not self.flip): self.velX = 1
            self.changeX = 1-self.baseSpeed - self.velX / 100
            
            self.flip = True
            self.running = True
            
        elif key[pygame.K_d]:
            if(self.flip): self.velX = 1
            self.changeX = self.baseSpeed + self.velX / 100
            
            self.flip = False
            self.running = True
            
        else: self.velX = 1
            
        if(self.velX < limitVelX):
            self.velX *= player_config["VERTICAL_ACCELERATION"]
        

    def leftRightBorderLimit(self, screenWidth):
        if self.body.left + self.changeX < 0:
            self.changeX = 0 - self.body.left
            
        if self.body.right + self.changeX > screenWidth:
            self.changeX = screenWidth - self.body.right
            self.readyForNextStage = True


    def jumpIfAllowed(self, key):
        if key[pygame.K_SPACE] and not self.jumping:
            self.velY -= player_config["JUMP_HEIGHT"]
            self.jumping = True
            
        self.velY += player_config["GRAVITY"]
        self.changeY += self.velY
        

    def attack(self, surface, target, damage):
        attackRange = pygame.Rect(self.body.centerx - self.body.width, self.body.top, self.body.width*2, self.body.height)
        if attackRange.colliderect(target.body):
            target.health -= damage
            target.hit = True
        
        
    def performAttackIfAllowed(self, key, surface: pygame.Surface, enemies):
        if key[pygame.K_w] and not self.attacking:
            self.attacking = True
            self.stagesDealingDamage = set()
        
        
    def getClosetEnemy(self, enemies):
        minDistance = inf
        closetEnemy = None
        for enemy in enemies:
            distance = sqrt(pow(self.body.x-enemy.body.x, 2) + pow(self.body.y-enemy.body.y, 2))
            if distance < minDistance:
                minDistance = distance
                closetEnemy = enemy
        return closetEnemy
import pygame
from math import inf, sqrt
from time import time
from config import playerConfig
from entity.entity import Entity


class Player(Entity):
    def __init__(self, x, y, playerSpritesheet, emp):
        super().__init__(x, y, playerSpritesheet, playerConfig)
        self.emp = emp
        self.empUsed = False
        
        self.velX = 1
        self.velY = 0
        self.baseSpeed = playerConfig["BASE_SPEED"]
        
        self.flip = False
        self.running = False
        self.jumping = False
        self.hit = False
        
        self.readyForNextStage = False
        
        self.stagesDealingDamage = set()
        
    def move(self, screenWidth, screenHeight, surface, enemies):
        self.readyForNextStage = False
        self.changeX = 0
        self.changeY = 0
        self.running = False
        key = pygame.key.get_pressed()
        
        self.__jumpIfAllowed(key)
        
        self.__performAttackIfAllowed(key, surface, enemies)
        
        self.__useEmpIfAvailable(key, surface, enemies)

        self.__verticalPlayerMovement(key, playerConfig["VERTICAL_ACCELERATION_LIMIT"])
        
        self.__leftRightBorderLimit(screenWidth)
            
        self.__groundLimit(screenHeight)
            
        self.body.x += self.changeX
        self.body.y += self.changeY
        
    
    def __useEmpIfAvailable(self, key, screen, enemies):
        if(not self.empUsed and key[pygame.K_s]):
            self.empUsed = True
            self.emp.body.x = self.body.x
            self.emp.body.y = self.body.y
            for enemy in enemies: self.__attack(screen, enemy, playerConfig["EMP_DAMAGE"])
        
        if(not self.emp.finished and self.empUsed):
            self.emp.draw(screen)
            self.emp.updateAnimation()
            self.empUsed = True
        
        
    def __groundLimit(self, screenHeight):
        if self.body.bottom + self.changeY > screenHeight - 50:
            self.velY = 0
            self.jumping = False
            self.changeY = screenHeight - 50 - self.body.bottom
        
        
    def updateAnimation(self, surface, enemies):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self._updateAction(playerConfig["ANIM_DEATH"])
        elif self.hit: self._updateAction(playerConfig["ANIM_HIT"])
        elif self.attacking: self._updateAction(playerConfig["ANIM_ATTACK"])
        elif self.jumping: self._updateAction(playerConfig["ANIM_JUMP"])
        elif self.running: self._updateAction(playerConfig["ANIM_RUN"])
        else: self._updateAction(playerConfig["ANIM_IDLE"])
        
        current = pygame.time.get_ticks()
        self.image = self.animationList[self.action][self.frameIndex]
        
        if current - self.lastAnimationUpdateTime > self.animationCooldown:
            self.frameIndex += 1
            self.lastAnimationUpdateTime = current
            
        if self.frameIndex >= len(self.animationList[self.action]):
            self.frameIndex = 0
            if self.action == playerConfig["ANIM_ATTACK"]:
                self.attacking = False
            elif self.action == playerConfig["ANIM_HIT"]:
                self.attacking = False
                self.hit = False
            elif self.alive == False:
                self.frameIndex = len(self.animationList[self.action]) - 1
                
        if self.action == playerConfig["ANIM_ATTACK"] and self.frameIndex % 4 == 0 and self.frameIndex not in self.stagesDealingDamage:
            if(len(enemies) > 0): self.__attack(surface, self.__getClosetEnemy(enemies), playerConfig["DAMAGE"])
            self.stagesDealingDamage.add(self.frameIndex)
            
     
    def __verticalPlayerMovement(self, key, limitVelX):
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
            self.velX *= playerConfig["VERTICAL_ACCELERATION"]
        

    def __leftRightBorderLimit(self, screenWidth):
        if self.body.left + self.changeX < 0:
            self.changeX = 0 - self.body.left
            
        if self.body.right + self.changeX > screenWidth:
            self.changeX = screenWidth - self.body.right
            self.readyForNextStage = True


    def __jumpIfAllowed(self, key):
        if key[pygame.K_SPACE] and not self.jumping:
            self.velY -= playerConfig["JUMP_HEIGHT"]
            self.jumping = True
            
        self.velY += playerConfig["GRAVITY"]
        self.changeY += self.velY
        

    def __attack(self, surface, target, damage):
        attackRange = pygame.Rect(self.body.centerx - self.body.width, self.body.top, self.body.width*2, self.body.height)
        if attackRange.colliderect(target.body):
            target.health -= damage
            target.hit = True
        
        
    def __performAttackIfAllowed(self, key, surface, enemies):
        if key[pygame.K_w] and not self.attacking:
            self.attacking = True
            self.stagesDealingDamage = set()
        
        
    def __getClosetEnemy(self, enemies):
        minDistance = inf
        closetEnemy = None
        for enemy in enemies:
            distance = sqrt(pow(self.body.x-enemy.body.x, 2) + pow(self.body.y-enemy.body.y, 2))
            if distance < minDistance:
                minDistance = distance
                closetEnemy = enemy
        return closetEnemy
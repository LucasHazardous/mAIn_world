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
        
        self.vel_x = 1
        self.vel_y = 0
        self.base_speed = player_config["BASE_SPEED"]

        self.health = player_config["BASE_HEALTH"]
        
        self.flip = False
        self.running = False
        self.jumping = False
        self.attacking = False
        self.hit = False
        self.alive = True
        
        self.readyForNextStage = False
        
        self.attack_stages = set()
        
    def move(self, screen_width: int, screen_height: int, surface: pygame.Surface, enemies: List):
        self.readyForNextStage = False
        self.change_x = 0
        self.change_y = 0
        self.running = False
        key = pygame.key.get_pressed()
        
        self.jumpIfAllowed(key)
        
        self.performAttackIfAllowed(key, surface, enemies)
        
        self.useEmpIfAvailable(key, surface, enemies)

        self.verticalPlayerMovement(key, player_config["VERTICAL_ACCELERATION_LIMIT"])
        
        self.leftRightBorderLimit(screen_width)
            
        self.groundLimit(screen_height)
            
        self.body.x += self.change_x
        self.body.y += self.change_y
        
    
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
        
        
    def groundLimit(self, screen_height):
        if self.body.bottom + self.change_y > screen_height - 50:
            self.vel_y = 0
            self.jumping = False
            self.change_y = screen_height - 50 - self.body.bottom
        
        
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
        self.image = self.animation_list[self.action][self.frame_index]
        
        if current - self.last_animation_update_time > self.animation_cooldown:
            self.frame_index += 1
            self.last_animation_update_time = current
            
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            if self.action == player_config["ANIM_ATTACK"]:
                self.attacking = False
            elif self.action == player_config["ANIM_HIT"]:
                self.attacking = False
                self.hit = False
            elif self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
                
        if self.action == player_config["ANIM_ATTACK"] and self.frame_index % 4 == 0 and self.frame_index not in self.attack_stages:
            if(len(enemies) > 0): self.attack(surface, self.getClosetEnemy(enemies), player_config["DAMAGE"])
            self.attack_stages.add(self.frame_index)
            
     
    def verticalPlayerMovement(self, key, vel_x_limit):
        if key[pygame.K_a]:
            if(not self.flip): self.vel_x = 1
            self.change_x = -self.base_speed - self.vel_x / 100
            
            self.flip = True
            self.running = True
            
        elif key[pygame.K_d]:
            if(self.flip): self.vel_x = 1
            self.change_x = self.base_speed + self.vel_x / 100
            
            self.flip = False
            self.running = True
            
        else: self.vel_x = 1
            
        if(self.vel_x < vel_x_limit):
            self.vel_x *= player_config["VERTICAL_ACCELERATION"]
        

    def leftRightBorderLimit(self, screen_width):
        if self.body.left + self.change_x < 0:
            self.change_x = 0 - self.body.left
            
        if self.body.right + self.change_x > screen_width:
            self.change_x = screen_width - self.body.right
            self.readyForNextStage = True


    def jumpIfAllowed(self, key):
        if key[pygame.K_SPACE] and not self.jumping:
            self.vel_y -= player_config["JUMP_HEIGHT"]
            self.jumping = True
            
        self.vel_y += player_config["GRAVITY"]
        self.change_y += self.vel_y
        

    def attack(self, surface, target, damage):
        attack_range = pygame.Rect(self.body.centerx - self.body.width, self.body.top, self.body.width*2, self.body.height)
        if attack_range.colliderect(target.body):
            target.health -= damage
            target.hit = True
        
        
    def performAttackIfAllowed(self, key, surface: pygame.Surface, enemies):
        if key[pygame.K_w] and not self.attacking:
            self.attacking = True
            self.attack_stages = set()
        
        
    def getClosetEnemy(self, enemies):
        min_distance = inf
        closet_enemy = None
        for enemy in enemies:
            distance = sqrt(pow(self.body.x-enemy.body.x, 2) + pow(self.body.y-enemy.body.y, 2))
            if distance < min_distance:
                min_distance = distance
                closet_enemy = enemy
        return closet_enemy
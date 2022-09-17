import pygame
from math import inf, sqrt
from typing import List
from time import time
from config import player_config

class Player():
    def __init__(self, x, y, flip, player_spritesheet):
        self.vel_x = 1
        self.vel_y = 0
        self.base_speed = player_config["BASE_SPEED"]

        self.health = player_config["BASE_HEALTH"]
        
        self.flip = flip
        self.running = False
        self.jumping = False
        self.attacking = False
        self.hit = False
        self.alive = True
        
        self.body = pygame.Rect((x, y, player_config["HITBOX_WIDTH"], player_config["HITBOX_HEIGHT"]))
        self.last_animation_update_time = pygame.time.get_ticks()
        self.animation_cooldown = player_config["ANIMATION_COOLDOWN"]
        self.size = player_config["PLAYER_SIZE"]
        self.image_scale = player_config["PLAYER_SCALE"]
        self.offset = player_config["PLAYER_OFFSET"]
        self.animation_list = self.load_images(player_spritesheet, player_config["PLAYER_ANIMATION_STEPS"])
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        
        self.attack_stages = set()
        
        
    def load_images(self, sprite_sheet: pygame.Surface, animation_steps):
        animation_list = []
        for j, animation in enumerate(animation_steps):
            temp_img_list = []
            for i in range(animation):
                temp_img = sprite_sheet.subsurface(i*self.size, j*self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size*self.image_scale, self.size*self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
        
    def move(self, screen_width: int, screen_height: int, surface: pygame.Surface, enemies: List):
        self.change_x = 0
        self.change_y = 0
        self.running = False
        key = pygame.key.get_pressed()
        
        if(key[pygame.K_p]): 
            self.hit = True
            self.health -= 10
        
        self.jumpIfAllowed(key)
        
        self.performAttackIfAllowed(key, surface, enemies)

        self.verticalPlayerMovement(key, player_config["VERTICAL_ACCELERATION_LIMIT"])
        
        self.leftRightBorderLimit(screen_width)
            
        self.groundLimit(screen_height)
            
        self.body.x += self.change_x
        self.body.y += self.change_y
        
        
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
            self.attack(surface, self.getClosetEnemy(enemies))
            self.attack_stages.add(self.frame_index)
                
            
    def updateAction(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.last_animation_update_time = pygame.time.get_ticks()
            
     
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


    def jumpIfAllowed(self, key):
        if key[pygame.K_SPACE] and not self.jumping:
            self.vel_y -= player_config["JUMP_HEIGHT"]
            self.jumping = True
            
        self.vel_y += player_config["PLAYER_GRAVITY"]
        self.change_y += self.vel_y
        

    def attack(self, surface, target):
        # self.attacking = True
        # self.body.right if not self.flip else self.body.left-self.body.width*2
        attack_range = pygame.Rect(self.body.centerx - self.body.width, self.body.top, self.body.width*2, self.body.height)
        if attack_range.colliderect(target.body):
            print(f"Attacked ${type(target).__name__}")
            target.health -= 10
            target.hit = True
        
        pygame.draw.rect(surface, (0,255,0), attack_range)
        
        
    def performAttackIfAllowed(self, key, surface: pygame.Surface, enemies):
        if key[pygame.K_w] and not self.attacking:
            self.attacking = True
            self.attack_stages = set()
            # self.attack(surface, self.getClosetEnemy(enemies))


    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.body)
        surface.blit(img, (self.body.x-self.offset[0]*self.image_scale, self.body.y-self.offset[1]*self.image_scale))
        
        
    def getClosetEnemy(self, enemies):
        min_distance = inf
        closet_enemy = None
        for enemy in enemies:
            distance = sqrt(pow(self.body.x-enemy.body.x, 2) + pow(self.body.y-enemy.body.y, 2))
            if distance < min_distance:
                min_distance = distance
                closet_enemy = enemy
        return closet_enemy
        
        
class Enemy():
    def __init__(self, x, y):
        self.health = 100
        self.body = pygame.Rect((x, y, 80, 180))
        self.hit = False
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.body)
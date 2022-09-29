from time import time
import pygame

class Entity():
    def __init__(self, x, y, entity_spritesheet, entity_config):
        self.base_health = entity_config["BASE_HEALTH"]
        self.health = self.base_health
        
        self.alive = True
        self.flip = True
        self.attacking = False
        
        self.last_animation_update_time = pygame.time.get_ticks()
        self.animation_cooldown = entity_config["ANIMATION_COOLDOWN"]
        self.size_x = entity_config["SIZE_X"]
        self.size_y = entity_config["SIZE_Y"]
        self.offset = entity_config["OFFSET"]
        
        self.body = pygame.Rect((x, y, entity_config["HITBOX_WIDTH"], entity_config["HITBOX_HEIGHT"]))
        self.image_scale = entity_config["SCALE"]
        self.action = 0
        self.frame_index = 0
        
        self.animation_list = self.load_images(entity_spritesheet, entity_config["ANIMATION_STEPS"])
    
        self.image = self.animation_list[self.action][self.frame_index]
    
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.body.x-self.offset[0]*self.image_scale, self.body.y-self.offset[1]*self.image_scale))
        
        
    def load_images(self, sprite_sheet: pygame.Surface, animation_steps):
        animation_list = []
        for j, animation in enumerate(animation_steps):
            temp_img_list = []
            for i in range(animation):
                temp_img = sprite_sheet.subsurface(i*self.size_x, j*self.size_y, self.size_x, self.size_y)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size_x*self.image_scale, self.size_y*self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
    
    
    def updateAction(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.last_animation_update_time = pygame.time.get_ticks()
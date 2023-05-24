import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

Y_POS = 300
Y_POS_DUCK = 340
JUMP_VEL = 8.5


class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 10
        self.dino_rect.y = Y_POS
        
        self.step_count = 0
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        
        self.jump_vel = JUMP_VEL
    
    def update(self, user_input):
        
        if user_input[pygame.K_UP] and not self.dino_jump and self.dino_rect.y == Y_POS:
            self.dino_run = False
            self.dino_jump = True
            
        if user_input[pygame.K_DOWN]:
            self.dino_duck = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_run = True
            
        if user_input[pygame.K_RIGHT]:
            self.dino_right = True
            self.dino_run = False

        elif user_input[pygame.K_LEFT]:
            self.dino_left = True
            self.dino_run = False
            
        if self.dino_run == True:
            self.run()
        elif self.dino_jump == True:
            self.jump()
        elif self.dino_duck == True:
            self.duck()
        elif self.dino_right == True:
            self.right()
        elif self.dino_left == True:
            self.left()
        
        if self.step_count > 3:
            self.step_count = 1
    
    def right(self):
        self.image = RUNNING[self.step_count//3]
        if self.dino_right == True:
            if self.dino_rect.x < 600:
                self.dino_rect.x += 10
            else:
                self.dino_right = False
            
        self.dino_right = False    
                      
        self.step_count += 1
        
    def left(self):
        self.image = RUNNING[self.step_count//3]
        if self.dino_left == True:
            if self.dino_rect.x > 10:
                self.dino_rect.x -= 10
            else:
                self.dino_left = False
                
        self.dino_left = False    
                      
        self.step_count += 1
    
    def run(self):
        self.image = RUNNING[self.step_count//3]
        self.dino_rect.y = Y_POS
        
        self.step_count+=1
    
    def duck(self):
        if self.dino_duck == True:
            self.image = DUCKING[self.step_count//3]
            self.dino_rect.y = Y_POS_DUCK
        
        self.dino_duck = False
        self.step_count+=1
    
    def jump(self):
        self.image = JUMPING
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8
            
        if self.jump_vel <- JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL
            
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))
        
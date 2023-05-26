import pygame

#pygame.init()
from time import sleep

from dino_runner.components.power_ups.power_up_manager import PowerUpManager

import random

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.shield import Shield


from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE, DEFAULT_TYPE, AUDIO, BACK, RUNNING_HAMMER, HAMMER

from dino_runner.components.dinosaur import Dinosaur

corBranca = (255,255,255)
corGrama = (32,181,25)
corCloud = (59,222,235)
receivCloud = CLOUD

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.cloud_y_pos = random.randint(290, 400)
        self.cloud_x_pos = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        self.executing = True
        self.obstacle_manager = ObstacleManager()
        self.score = 0
        self.death_count = 0

        self.shield = Shield

        self.musicFundo = AUDIO
        
        self.player = Dinosaur()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.back_width = BACK

        self.power_up_manager = PowerUpManager()

        
    def restart(self):
        self.playing = False
        self.executing = False
        self.execute()  
    
    def execute(self):
        if self.playing and self.executing:
            self.display_menu()
             
        while self.executing == True:
            
            if not self.playing:
                self.display_menu()
        
        while self.executing == False:
            if not self.playing:
                self.menuContenue()
                
    

    def run(self):
        pygame.mixer.music.play(3)
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
                self.executing = False


    def update(self):
        dinohammershield = 0
        user_input = pygame.key.get_pressed()
        if self.score >= 100:
            dinohammershield = random.randint(1,2)
            self.player.update(user_input, dinohammershield)
            self.shield
        else:
            self.player.update(user_input, dinohammershield)
        self.update_score()
        self.update_speed()
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        

        
        

    def update_score(self):
            self.score += 1
                
            
    def update_speed(self):
        if self.score % 100 == 0:
            self.plus = int(random.choice([1, 2, 3]))
            self.game_speed += self.plus

            if self.game_speed >= 60:
                self.game_speed = 60
    
    def scren_speed(self):
        font = pygame.font.Font(FONT_STYLE, 20)
        textSpeed = font.render(f"Speed: {self.game_speed} Km/h", True, (0,0,0))
        textSpeed_rect = textSpeed.get_rect()
        textSpeed_rect.center = (1200, 50)
        self.screen.blit(textSpeed, textSpeed_rect)



    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((97,97,97))
        self.draw_background()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_simple_cloud()
        pygame.display.update()
        pygame.display.flip()
        
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000,2)
            
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up Time:{time_to_show}s", True, (255,0,0))
                
                text_rect = text.get_rect()
                text_rect.x = 500
                text_rect.y = 50
                
                self.screen.blit(text, text_rect)
                
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE


    def display_menu(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press any key to start", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)
        
        self.screen.blit(text, text_rect)
        self.menu_events_handler()
        pygame.display.update()
        
    def menu_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
                self.menuContenue()
                
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1200,70)
        
        self.screen.blit(text, text_rect)
        


    def draw_background(self):
        self.screen.blit(self.back_width, (0, 0))
        self.draw_score()
        self.scren_speed()
        self.x_pos_bg -= self.game_speed

        
    
    def draw_simple_cloud(self):
        cloud_image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        if self.cloud_x_pos <= -cloud_image_width:
            self.cloud_x_pos = SCREEN_WIDTH + random.randint(0,50)
            self.cloud_y_pos = random.randint(160, 240)
            self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        self.cloud_x_pos -= self.game_speed
        
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20
        
    def menuContenue(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2

        font = pygame.font.Font(FONT_STYLE, 22)
        textCont = font.render("Press C to continue", True, (0,0,0))
        textCont2 = font.render("Press R to restart", True, (0,0,0))
        textCont3 = font.render("Press SPACE to exit", True, (0,0,0))
        textCont_rect = textCont.get_rect()
        textCont_rect.center = (x_text_pos, y_text_pos)
        textCont2_rect = textCont2.get_rect()
        textCont2_rect.center = ((x_text_pos, y_text_pos * 1.2))
        textCont3_rect = textCont3.get_rect()
        textCont3_rect.center = ((x_text_pos, y_text_pos * 1.4))
        
        self.screen.blit(textCont, textCont_rect)
        self.screen.blit(textCont2, textCont2_rect)
        self.screen.blit(textCont3, textCont3_rect)
        
        
        self.optionToContinue()
        pygame.display.update()
        pygame.display.flip()
        
    def optionToContinue(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                user_input = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        #self.player.update(user_input)
                        self.obstacle_manager.reset_obstacles()
                        self.run()
                    elif event.key == pygame.K_r:
                        self.reset_game()
                        self.run()
                    else:
                        exit()
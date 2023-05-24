import pygame

<<<<<<< Updated upstream
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur

=======

pygame.init()


import random

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE

from dino_runner.components.dinosaur import Dinosaur

corBranca = (255,255,255)
corGrama = (32,181,25)
corCloud = (59,222,235)
receivCloud = CLOUD


>>>>>>> Stashed changes
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
<<<<<<< Updated upstream
        
=======
        self.cloud_y_pos = random.randint(100, 250)
        self.cloud_x_pos = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        self.executing = True
       
        self.obstacle_manager = ObstacleManager()
        self.score = 0
        self.death_count = 0
>>>>>>> Stashed changes
        self.player = Dinosaur()
        
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
<<<<<<< Updated upstream

=======
        
    def restart(self):
        self.playing = False
        self.executing = False
        self.execute()  
    
    def execute(self):
        
        if self.executing == False and self.playing == False:
            self.executing = True
            self.playing = True
            self.menuContenue()
        
        while self.executing == True:
            
            if not self.playing:
                self.display_menu()  
    
>>>>>>> Stashed changes
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #self.menuContenue()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
<<<<<<< Updated upstream
                
=======
                self.executing = False

>>>>>>> Stashed changes
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        

<<<<<<< Updated upstream
=======

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
        textSpeed_rect.center = (1020, 50)
        self.screen.blit(textSpeed, textSpeed_rect)


>>>>>>> Stashed changes
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        
        pygame.display.flip()

<<<<<<< Updated upstream
=======

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
        #pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        #pygame.display.flip()
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
        text_rect.center = (1030,70)
        
        
        self.screen.blit(text, text_rect)
    
>>>>>>> Stashed changes
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
<<<<<<< Updated upstream
=======
        #pygame.display.set_caption("Km/h")
        
    
    def draw_simple_cloud(self):
        cloud_image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        if self.cloud_x_pos <= -cloud_image_width:
            self.cloud_x_pos = SCREEN_WIDTH + random.randint(0,50)
            self.cloud_y_pos = random.randint(50, 250)
            self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        self.cloud_x_pos -=self.game_speed
        
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20
        
    def menuContenue(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2

        font = pygame.font.Font(FONT_STYLE, 22)
        textCont = font.render("Press C to continue ", True, (0,0,0))
        textCont2 = font.render("Press R to restart", True, (0,0,0))
        textCont_rect = textCont.get_rect()
        textCont_rect.center = (x_text_pos, y_text_pos)
        textCont2_rect = textCont2.get_rect()
        textCont2_rect.center = ((x_text_pos, y_text_pos * 1.2))
        
        self.screen.blit(textCont, textCont_rect)
        self.screen.blit(textCont2, textCont2_rect)
        
        self.optionToContinue()
        pygame.display.update()
        #pygame.display.flip()
        
    def optionToContinue(self):
        user_input = pygame.key.get_pressed()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            
            if user_input[pygame.K_c]:
                print("chegou")
                self.run()
            
        
            
        if user_input[pygame.K_r]:
            self.__init__()
                          
>>>>>>> Stashed changes

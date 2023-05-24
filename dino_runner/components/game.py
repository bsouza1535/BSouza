import pygame

import random

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, BIRD1, FONT_STYLE

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.options import Menu

corBranca = (255,255,255)
corGrama = (32,181,25)
corCloud = (59,222,235)
receivCloud = CLOUD
receivBird = BIRD1


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.cloud_y_pos = random.randint(100, 250)
        self.cloud_x_pos = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        
        self.cloud = []
        self.bird = []
        self.obstacle_manager = ObstacleManager()
        self.score = 0
        self.death_count = 0
        self.player = Dinosaur()
        self.texto_km = pygame.font.SysFont("Arial", 20, True, False)
        
        self.playing = False
        self.game_speed = 15
        
        
        self.x_pos_bg = 0
        self.y_pos_bg = 380
    def execute(self):
        self.executing = True
        while self.executing:
            
            if not self.playing:
                self.display_menu()
        
        pygame.quit()    
    
    def run(self):
        self.playing = True
        while self.playing == True:
            self.events()
            self.update()
            self.draw()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):

        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.update_speed()
        self.obstacle_manager.update(self)

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
    """    
    def screen_km(self):
        self.textKm = self.texto_km.render("Km/h", 0, corBranca)
        self.screen.blit(self.textKm, (1025, 50))
 """
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((97,97,97))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_simple_cloud()
        pygame.display.update()
        pygame.display.flip()


    def display_menu(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press any key to start", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)
        
        self.screen.blit(text, text_rect)
        #print(self.death_count)
        
        self.menu_events_handler()
        pygame.display.flip()
        
    def menu_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
                
    def draw_score(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1030,70)
        
        
        self.screen.blit(text, text_rect)
    
    def draw_background(self):
        image_width = BG.get_width()
        BG.fill(corGrama)
        self.draw_score()
        self.scren_speed()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        pygame.display.set_caption("Km/h")
        
    
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
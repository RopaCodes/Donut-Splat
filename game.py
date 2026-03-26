import pygame
from settings import WIDTH, HEIGHT
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT
        self.background = pygame.image.load("assets/bg_img2.png")

        
         # lives rendering
        self.lives = 5
        self.game_font = pygame.font.Font("assets/Somelist.ttf", 40)

        #screen state rendering
        self.start_men = pygame.image.load("assets/menu_screen.PNG")
        self.game_head_font = pygame.font.Font("assets/Somelist.ttf", 80)
        
    def draw_items(self):
        self.screen.blit(self.background,(0,0))
        
    
    def update_lives_left(self, donut_miss):
        lives_left_text = self.game_font.render("Lives: "+ str(self.lives),True,(0, 0, 0))
        self.screen.blit(lives_left_text,(30,10))
        if donut_miss:
            self.lives -= 1
    
    def reset_lives(self):
        self.lives = 5
        


    def draw_start_screen(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.start_men,(0,0))
        start_title = self.game_head_font.render("Donut",True,(0, 1, 0))
        start_title2 = self.game_head_font.render("Splash",True,(0, 1, 0))
        play_game_text = self.game_font.render("Press enter to start", True, (0,0,0))
        self.screen.blit(start_title,(30,40))
        self.screen.blit(start_title2,(30,130))
        self.screen.blit(play_game_text,(200,(HEIGHT-70)))
        
        

    def draw_gameover_screen(self, high_score):
        
        play_game_text = self.game_font.render("Press enter to replay", True, (0,0,0))
        self.screen.blit(self.background,(0,0))
        game_over_title = self.game_head_font.render("Game Over",True,(0, 0, 0))
        high_score_text = self.game_font.render("High Score: "+ str(high_score), True, (0,0,0))

        self.screen.blit(game_over_title,((WIDTH//2)-230,(HEIGHT//2)-200))
        self.screen.blit(play_game_text,((WIDTH//2)-230,(HEIGHT//2)-100))
        self.screen.blit(high_score_text,((WIDTH//2)-160,(HEIGHT//2)))
    
    

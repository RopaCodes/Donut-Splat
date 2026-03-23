import pygame
from settings import WIDTH, HEIGHT
pygame.init()
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT
        self.background = pygame.image.load("assets/bg_img2.png")

    def draw_items(self):
        self.screen.blit(self.background,(0,0))
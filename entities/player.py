import pygame, os
from settings import WIDTH, HEIGHT
pygame.init()

class PipingPlayer:
    def __init__(self,screen):
        self.screen = screen
        
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.img_path = os.path.join(self.base_dir, '..', 'assets', 'piping_bag.PNG')
        
        # load spritesheet
        self.player_img = pygame.image.load(self.img_path).convert_alpha()
        self.sheet_width, self.sheet_height = self.player_img.get_size()

        #frame dimensions
        self.num_of_frames = 4
        self.frame_width = self.sheet_width // self.num_of_frames
        self.frame_height = self.sheet_height

        # crop and scale one frame
        # frame_rect = pygame.Rect(self.frame_width*3, 0, self.frame_width, self.frame_height)
        frame_rect = pygame.Rect(0, 0, self.frame_width, self.frame_height)
        frame = self.player_img.subsurface(frame_rect) #cuts out that piece and returns it as its own surface (image)

        self.display_width = 130
        self.scale_ratio = self.display_width / self.frame_width
        self.display_height = int(self.frame_height*self.scale_ratio)
  
        self.scaled_frame = pygame.transform.scale(frame, (self.display_width, self.display_height))

        self.x_pos = (WIDTH/2)-(self.display_width/2)
        self.y_pos = HEIGHT-(self.display_height)

        self.speed = 4

    def draw_item(self):
        self.screen.blit(self.scaled_frame,(self.x_pos,self.y_pos))
    
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x_pos -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x_pos += self.speed
        # if keys[pygame.K_SPACE]:



    

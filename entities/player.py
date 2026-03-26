import pygame, os
from settings import WIDTH, HEIGHT
pygame.init()

class PipingPlayer:
    def __init__(self, screen):
        self.screen = screen
        
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.img_path = os.path.normpath(os.path.join(self.base_dir, '..', 'assets', 'piping_bag.PNG'))
        
        # load spritesheet
        self.player_img = pygame.image.load(self.img_path).convert_alpha()
        self.sheet_width, self.sheet_height = self.player_img.get_size()

        # frame dimensions
        self.num_of_frames = 4
        self.frame_width = self.sheet_width // self.num_of_frames
        self.frame_height = self.sheet_height

        # pre-crop and scale all frames into a list
        self.frames = [] # get al frames of spritesheet in here
        for i in range(self.num_of_frames):
            frame_rect = pygame.Rect(i * self.frame_width, 0, self.frame_width, self.frame_height)
            frame = self.player_img.subsurface(frame_rect)

            display_width = 130
            scale_ratio = display_width / self.frame_width
            display_height = int(self.frame_height * scale_ratio)

            scaled = pygame.transform.smoothscale(frame, (display_width, display_height))
            self.frames.append(scaled) #so each time the loop runs it wil be different

        self.display_width = 130
        self.display_height = int(self.frame_height * (self.display_width / self.frame_width))

        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 6  # frames between each sprite change, increase to slow down

        self.x_pos = (WIDTH / 2) - (self.display_width / 2)
        self.y_pos = HEIGHT - self.display_height

        self.speed = 4  #speed for player movement
        self.shoot_animation_active = False

    def draw_item(self):
        self.screen.blit(self.frames[self.frame_index], (self.x_pos, self.y_pos))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x_pos -= self.speed 
            #check boundary
            if self.x_pos <= (0-self.display_width/2+31):
                self.x_pos = 0-self.display_width/2+31
        
        if keys[pygame.K_RIGHT]:
            self.x_pos += self.speed
            #check boundary
            if self.x_pos >= WIDTH-(self.display_width)+27:
                self.x_pos = WIDTH-(self.display_width)+27

        
        

        if keys[pygame.K_SPACE]:
            self.shoot_animation_active = True

        if self.shoot_animation_active:
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed: #has to wait 6 ticks b4 showing the frame changing on screen, so every 6 ticks
                self.animation_timer = 0
                self.frame_index += 1
                if self.frame_index >= len(self.frames):
                    self.frame_index = 0
                    self.shoot_animation_active = False  # stop after one full cycle

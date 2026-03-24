import pygame, os
from settings import WIDTH, HEIGHT
pygame.init()

class Projectile:
    def __init__(self,screen):
        self.screen = screen
        
        self.diemnsions = 50

        #bullet stats
        self.speed = 3
        self.bullets = []
        
        self.key_pressed = False

        # load img
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.img_path = os.path.normpath(os.path.join(self.base_dir, '..', 'assets', 'frosting_bullet.PNG'))
        self.bullet_img = pygame.image.load(self.img_path)
        self.bullet_rect = self.bullet_img.get_rect()
        self.scaled_bullet = pygame.transform.smoothscale(self.bullet_img, (self.diemnsions, self.diemnsions))

    def update(self, keys,bag_posX, bag_posY):
        # Detect if 'SPACE' was just clicked (once)
        #if keys[pygame.K_SPACE]:
            #self.bullets.append(self.scaled_bullet)
            #print(len(self.bullets))
        if keys[pygame.K_SPACE]:
            if not self.key_pressed:
                    # ACTION TRIGGERED ONLY ONCE
                    self.bullets.append([self.scaled_bullet, bag_posX + 50, bag_posY - 7])
                    self.key_pressed = True  # Set state to "held
                    
        if not keys[pygame.K_SPACE]:
             self.key_pressed = False
        
        # in your update/draw loop
        for bullet in self.bullets:
            bullet[2] -= self.speed  # move each bullet up independently
            self.screen.blit(bullet[0], (bullet[1], bullet[2]))
                

    


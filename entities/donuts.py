import pygame, os, random
from settings import WIDTH, HEIGHT

pygame.init()

class Donuts:
    def __init__(self,screen):
        self.screen = screen

        self.base_falling_speed = 2
        self.spawn_timer = 0
        self.spawn_speed = 60 # spawn new donut every second, lower = more
        
        self.y_pos = 0
        self.game_running = True

        #soundfx
        self.donut_hit = pygame.mixer.Sound("assets/soundFX/donut_hit.wav")
        
    
        self.animation_timer = 0
        self.animation_speed = 6  # frames between each sprite change, increase to slow down
        self.donut_missed = False

        self.high_score = 0


        # load img
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.filenames = ['extra_donut_1.PNG',
                           'extra_donut_2.PNG',
                            'extra_donut_3.PNG',
                            'golden_donut_1.PNG',
                            'golden_donut_2.PNG',
                            'golden_donut_3.PNG',
                            'base_donut_1.PNG',
                            'base_donut_2.PNG']
        self.scaled_donut_imgs = []
        self.donut_imgs = []
        self.active_donuts = []
        
        for filename in self.filenames:
            path = os.path.normpath(os.path.join(self.base_dir, '..','assets',filename))
            new_donut_img = pygame.image.load(path).convert_alpha()
            self.donut_imgs.append(new_donut_img)

        for i in range(len(self.donut_imgs)):
            dimensions = 50
            scaled = pygame.transform.smoothscale(self.donut_imgs[i], (dimensions, dimensions))
            
            self.scaled_donut_imgs.append(scaled) #so each time the loop runs it wil be different

    def update(self, bullets): #donut spwaning and drawing function
        self.donut_missed = False
        # spawn a new donut every N ticks
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_speed:
            self.spawn_timer = 0 #reset timer for spawning
            x_pos = random.randint(10, WIDTH - 100)
            new_donut = [random.choice(self.scaled_donut_imgs), x_pos, 0]
            self.active_donuts.append(new_donut)

        # move each donut down and draw it
        for donut in self.active_donuts:
            
            donut[2] += self.base_falling_speed
            self.screen.blit(donut[0], (donut[1], donut[2]))
            donut_rect = donut[0].get_rect(topleft=(donut[1],donut[2]))

            for bullet in bullets[:]: #looping over a copy of the bullets list
                bullet_rect = bullet[0].get_rect(topleft = (bullet[1], bullet[2]))
                if donut_rect.colliderect(bullet_rect): #if collides with icing bullet
                    self.high_score += 10
                    self.donut_hit.play()
                    self.active_donuts.remove(donut)   #removing from the original
                    bullets.remove(bullet)
                    
                    break

        # remove donuts that have fallen off screen
        new_list = []
        for d in self.active_donuts:
            if d[2] < HEIGHT:
                
                new_list.append(d)
                
            else:
                self.donut_missed = True
                   
        self.active_donuts = new_list #rebuilding the list to onl include donuts that are within the screen ehight
        return self.donut_missed


import pygame, sys
from settings import WIDTH, HEIGHT, FPS
from game import Game
from entities.player import PipingPlayer
from entities.projectile import Projectile
from entities.donuts import Donuts



def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    running = True
    game_state = "menu"  # start on menu

    #soundfx
    pygame.mixer.music.load("assets/soundFX/gameplay.wav") #meant for background track
    pygame.mixer.music.play(-1)

    start_sound = pygame.mixer.Sound("assets/soundFX/start_sound.wav") #use this format for sound effects
    game_over = pygame.mixer.Sound("assets/soundFX/game_over.wav") #use this format for sound effects

    # class objects
    game = Game(SCREEN)
    player = PipingPlayer(SCREEN)
    projectile = Projectile(SCREEN)
    donuts = Donuts(SCREEN)
    
    while running:
        #gameplay.play(-1)
        
        high_score = donuts.high_score
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    if game_state == "menu":
                        start_sound.play()
                        game_state = "playing"
                    elif game_state == "gameover":
                        
                        game.reset_lives()
                        #reset lists tp be empty again
                        donuts.active_donuts = [] 
                        projectile.bullets = []
                        game_state = "playing"
                        donuts.high_score = 0

        
        # draw based on current state
        if game_state == "menu":
            game.draw_start_screen()

        elif game_state == "playing":
            
            game.draw_items()
            keys = pygame.key.get_pressed()
            player.update(keys)
            player.draw_item()
            projectile.update(keys, player.x_pos, player.y_pos)
            donuts.update(projectile.bullets)
            game.update_lives_left(donuts.donut_missed)

            if game.lives <= 0:
                game_state = "gameover"
                game_over.play()
                

        elif game_state == "gameover":
            
            game.draw_gameover_screen(high_score)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

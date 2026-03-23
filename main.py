import pygame, sys
from settings import WIDTH, HEIGHT, FPS
from game import Game
from entities.player import PipingPlayer

def main():
    # pygame setup
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

    clock = pygame.time.Clock()
    running = True

    #class objects - must be created only once so outside the while loop
    game = Game(SCREEN)
    player = PipingPlayer(SCREEN)
    

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Handles keyboard events
                if event.key == pygame.K_ESCAPE:
                    # Quits the loop if the Escape key is pressed
                    running = False
                    
                    sys.exit()

        

        # calling functions 
        game.draw_items()
        keys = pygame.key.get_pressed()
        player.update(keys)
        player.draw_item()
        
        

        # updating
        
        pygame.display.update()
        clock.tick(FPS) 

if __name__ == "__main__":
    main()
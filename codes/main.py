import pygame, sys
from settings import *


class Game:
    def __init__(self):
        pass

    def run(self):
        pass
    # Update all sprite groups
    # Draw all sprite groups


if __name__ == '__main__':
    game = Game()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Background Color
        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)  # Framerate

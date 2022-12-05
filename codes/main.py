import pygame, sys
from settings import *
from player import *


class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(screen)
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

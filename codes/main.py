import pygame, sys
from settings import *
from player import *
import wall


class Game:
    def __init__(self):
        # Player
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Enemy
        self.shape = wall.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.create_obstacle(40, 480)

    def create_obstacle(self, x_start, y_start):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size
                    y = y_start + row_index * self.block_size
                    block = wall.Block(self.block_size, (224, 255, 255), x, y)
                    self.blocks.add(block)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
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

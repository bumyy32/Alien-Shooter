import pygame
import sys
from settings import *
from player import *
from aliens import *
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
        self.obstacle_amount = 7
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.multiple_obstacles(screen_width / 20, 600, *self.obstacle_x_positions)
        # self.multiple_obstacles(x_start, y_start, offset_x)
        # the * before self_obstacle_x_pos means that we're unpacking the list created.

        # Aliens!
        self.aliens = pygame.sprite.Group()
        self.aliens_setup(rows=1, cols=1)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = wall.Block(self.block_size, (224, 255, 255), x, y)
                    self.blocks.add(block)

    def multiple_obstacles(self, x_start, y_start, *offset):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def aliens_setup(self, rows, cols, x_distance=120, y_distance=80):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance
                y = row_index * y_distance
                aliens_sprite = Alien('red', x, y)
                self.aliens.add(aliens_sprite)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
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

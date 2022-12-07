import pygame


class Alien(pygame.sprite.Sprite):
    def __int__(self, color, x, y):
        super().__init__()
        file_path = '../graphics/enemies/' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

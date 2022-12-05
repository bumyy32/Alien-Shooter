import pygame, sys
from settings import *

screen_width = 1280 # X
screen_height = 720 # Y
screen = pygame.display.set_mode((screen_width, screen_height)) # Create display
clock = pygame.time.Clock() # Framerate
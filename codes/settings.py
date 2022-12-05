import pygame, sys

screen_width = 1280 # X
screen_height = 720 # Y
screen = pygame.display.set_mode((screen_width, screen_height)) # Create display
clock = pygame.time.Clock() # Framerate

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Background Color
    screen.fill((30, 30, 30))

    pygame.display.flip()
    clock.tick(60) #Framerate
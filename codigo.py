import pygame

# initialize pygame
pygame.init()

# create a window
window = pygame.display.set_mode((800, 600))

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw everything

    pygame.display.update()

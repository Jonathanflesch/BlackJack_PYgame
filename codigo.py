import sys
import pygame

# initialize pygame
pygame.init()

# create a window
branco = pygame.Color('grey100')
width = 1000
height = 700
window = pygame.display.set_mode((width, height))
#Imagens----------------------------------
banner = pygame.image.load('fundo.png/bj_banner_yellow2.png').convert_alpha()
banner = pygame.transform.scale(banner,(500,300))
caixa = pygame.image.load('fundo.png/yellow_box_179_120.png').convert_alpha()
caixa = pygame.transform.scale(caixa,(100,150))
caixa2 = pygame.image.load('fundo.png/yellow_box_179_120.png').convert_alpha()
caixa2 = pygame.transform.scale(caixa,(100,150))
background_img = pygame.image.load('fundo.png/Fundoverdeblack.png').convert()
background_img = pygame.transform.scale(background_img, (width, height))
# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw everything
    window.fill((255,255,255))
    window.blit(background_img, (0,0))
    window.blit(banner, (265,130))
    window.blit(caixa,(450,500))
    window.blit(caixa2,(450,50))
    pygame.display.update()

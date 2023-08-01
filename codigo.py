import sys
import pygame

# initialize pygame
pygame.init()
# create a window
preto = pygame.Color('grey0')
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
#Fonte e textos----------------------------------
fonte_inicial = pygame.font.Font('NeonSans.ttf', 100)
texto_ini = fonte_inicial.render('BlackJack',False,preto)
Barra_txt = fonte_inicial.render('Pressione Espaço', False,preto)
Barra2_txt = fonte_inicial.render('para começar', False,preto)
#TELA_DE_INICIO----------------------------------------------
inicial = True
while inicial:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicial = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                inicial = False
    window.fill((branco))
    window.blit(texto_ini, (280, 10 ))
    window.blit(Barra_txt, (10, 200))
    window.blit(Barra2_txt, (10, 300))
    pygame.display.update()
#game_loop---------------------------------------
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

import sys
import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
width = 1000
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Blackjack')

# Cores
preto = pygame.Color('black')
branco = pygame.Color('white')

# Imagens
# ... (o restante das imagens carregadas anteriormente)
fonte_inicial = pygame.font.Font('NeonSans.ttf', 100)
texto_ini = fonte_inicial.render('BlackJack',False,preto)
Barra_txt = fonte_inicial.render('Pressione Espaço', False,preto)
Barra2_txt = fonte_inicial.render('para começar', False,preto)

# Dicionário com as cartas e seus valores
valores_cartas = {
    'ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'jack': 10, 'queen': 10, 'king': 10
}

# Função para calcular o valor da mão do jogador
def calcular_valor_mao(mao):
    valor_total = sum([valores_cartas[carta] for carta in mao])
    # Verificação para o caso do Ás (se o valor total for menor ou igual a 11, o Ás vale 11)
    if 'ace' in mao and valor_total <= 11:
        valor_total += 10
    return valor_total

# Função para exibir a mensagem na tela
def exibir_mensagem(texto, tamanho, posicao):
    fonte = pygame.font.Font(None, tamanho)
    texto_renderizado = fonte.render(texto, True, preto)
    window.blit(texto_renderizado, posicao)

# Função para o jogo Blackjack
def blackjack_game():
    # Variáveis para controlar o estado do jogo
    jogador_mao = []
    cpu_mao = []
    jogador_dinheiro = 500
    aposta = 0
    jogando = True

    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Lógica do jogo aqui

        # Iniciar uma nova rodada (limpar as mãos e distribuir cartas)
        jogador_mao.clear()
        cpu_mao.clear()
        jogador_mao.append(random.choice(valores_cartas))
        cpu_mao.append(random.choice(valores_cartas))

        # Perguntar ao jogador quanto deseja apostar
        while True:
            window.fill(branco)
            exibir_mensagem('Blackjack', 64, (400, 50))
            exibir_mensagem('Dinheiro: $' + str(jogador_dinheiro), 32, (400, 100))
            exibir_mensagem('Quanto você quer apostar?', 32, (400, 200))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        aposta = 1
                    elif event.key == pygame.K_5:
                        aposta = 5
                    elif event.key == pygame.K_10:
                        aposta = 10
                    elif event.key == pygame.K_50:
                        aposta = 50
                    elif event.key == pygame.K_100:
                        aposta = 100
                    elif event.key == pygame.K_RETURN:
                        # Verificar se a aposta é válida
                        if aposta <= jogador_dinheiro:
                            jogando = False
                        else:
                            exibir_mensagem('Aposta inválida! Você não tem dinheiro suficiente.', 24, (400, 250))
                            pygame.display.update()
                            pygame.time.delay(1000)

        # Distribuir mais duas cartas para o jogador e a CPU
        jogador_mao.append(random.choice(lista_numeros))
        cpu_mao.append(random.choice(lista_numeros))

        # Loop para a vez do jogador
        jogador_jogando = True
        while jogador_jogando:
            window.fill(branco)
            exibir_mensagem('Blackjack', 64, (400, 50))
            exibir_mensagem('Dinheiro: $' + str(jogador_dinheiro), 32, (400, 100))
            exibir_mensagem('Aposta: $' + str(aposta), 32, (400, 150))
            exibir_mensagem('Sua mão: ' + ', '.join(jogador_mao), 32, (400, 200))
            exibir_mensagem('Valor: ' + str(calcular_valor_mao(jogador_mao)), 32, (400, 250))
            exibir_mensagem('Pressione "H" para pedir carta ou "F" para ficar', 24, (400, 300))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        jogador_mao.append(random.choice(lista_numeros))
                        valor_mao_jogador = calcular_valor_mao(jogador_mao)
                        # Verificar se o jogador estourou (valor maior que 21)
                        if valor_mao_jogador > 21:
                            jogador_dinheiro -= aposta
                            exibir_mensagem('Você estourou! Perdeu $' + str(aposta), 24, (400, 350))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            jogador_jogando = False
                    elif event.key == pygame.K_f:
                        jogador_jogando = False

        # Loop para a vez da CPU
        while calcular_valor_mao(cpu_mao) < 17:
            cpu_mao.append(random.choice(lista_numeros))

        # Verificar resultado
        valor_mao_jogador = calcular_valor_mao(jogador_mao)
        valor_mao_cpu = calcular_valor_mao(cpu_mao)

        window.fill(branco)
        exibir_mensagem('Blackjack', 64, (400, 50))
        exibir_mensagem('Dinheiro: $' + str(jogador_dinheiro), 32, (400, 100))
        exibir_mensagem('Aposta: $' + str(aposta), 32, (400, 150))
        exibir_mensagem('Sua mão: ' + ', '.join(jogador_mao), 32, (400, 200))
        exibir_mensagem('Valor: ' + str(valor_mao_jogador), 32, (400, 250))
        exibir_mensagem('Mão da CPU: ' + ', '.join(cpu_mao), 32, (400, 300))
        exibir_mensagem('Valor da CPU: ' + str(valor_mao_cpu), 32, (400, 350))

        # Verificar o resultado
        if valor_mao_jogador > 21 or (valor_mao_cpu <= 21 and valor_mao_cpu >= valor_mao_jogador):
            jogador_dinheiro -= aposta
            exibir_mensagem('Você perdeu $' + str(aposta), 24, (400, 400))
        else:
            jogador_dinheiro += aposta
            exibir_mensagem('Você ganhou $' + str(aposta), 24, (400, 400))

        pygame.display.update()
        pygame.time.delay(2000)

# Tela de início
inicial = True
while inicial:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicial = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                inicial = False

    window.fill(branco)
    window.blit(texto_ini, (280, 10 ))
    window.blit(Barra_txt, (10, 200))
    window.blit(Barra2_txt, (10, 300))
    pygame.display.update()

# Game loop
while True:
    blackjack_game()

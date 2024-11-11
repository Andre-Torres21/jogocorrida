import pygame
from scripts.cenas import *

pygame.init()

tamanho_tela = [600, 400]
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Jogo de corrida')
relogio = pygame.time.Clock()
cor_fundo = (86, 86, 86)

lista_cenas = {
    'partida': Partida(tela),
    'menu': Menu(tela)
}

cena_atual = 'menu'

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    tela.fill(cor_fundo)

    cena_atual = lista_cenas[cena_atual].atualizar()

    relogio.tick(60)
    pygame.display.flip()
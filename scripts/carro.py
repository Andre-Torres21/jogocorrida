import pygame

class Carro:
    def __init__(self, tela, x, y):
        self.posicao = [x, y]
        self.tamanho = [50, 50]
        self.rect = pygame.Rect(self.posicao, self.tamanho)
        
        self.tela = tela
        
        self.imagem = pygame.image.load('assets/carro.png')
        self.imagem = pygame.transform.scale(self.imagem, self.tamanho)
        self.imagem = pygame.transform.rotate(self.imagem, -90)
        
        self.velocidade_vertical = 5

    def desenhar(self):
        self.tela.blit(self.imagem, self.posicao)

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.posicao[1] = max(0, self.posicao[1] - self.velocidade_vertical)
        if teclas[pygame.K_DOWN]:
            self.posicao[1] = min(self.tela.get_height() - self.tamanho[1], self.posicao[1] + self.velocidade_vertical)
        
        self.rect = pygame.Rect(self.posicao, self.tamanho)

    def getRect(self):
        return pygame.Rect(self.posicao, self.tamanho)
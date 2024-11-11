import pygame
import random

class Cone:
    def __init__(self, tela):
        self.tamanho = [50, 50]
        self.imagem = pygame.image.load('assets/cone.png')
        self.imagem = pygame.transform.scale(self.imagem, self.tamanho) 
        self.tela = tela
        self.altura_base = random.randint(0, 400)
        self.x = tela.get_width()
        self.velocidade = 3
    
    def atualizar(self):
        self.x -= self.velocidade
        if self.x < -self.imagem.get_width():
            self.x = self.tela.get_width()
            self.altura_base = random.randint(10, 390)
            
    def desenhar(self):
        self.tela.blit(self.imagem, (self.x, self.altura_base))
        
    def detectar_colisao(self, rect_carro):
        rect_cone = pygame.Rect((self.x, self.altura_base), self.imagem.get_size())
        
        if rect_carro.colliderect(rect_cone):
            return True
        
        else:
            return False
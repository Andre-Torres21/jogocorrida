import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho
        
        pygame.font.init()
        self.fonte = pygame.font.Font(None, self.tamanho)
        self.imagem_texto = self.fonte.render(self.texto, False, self.cor)

    def desenhar(self):
        self.tela.blit(self.imagem_texto, self.posicao)

    def atualizar_texto(self, novo_texto):
        self.imagem_texto = self.fonte.render(novo_texto, False, self.cor)
        
class Botao:
    def __init__(self, tela, texto, x, y, tamanho, cor_fundo, cor_texto):
        self.tela = tela
        self.texto = Texto(tela, texto, x, y, cor_texto, tamanho)
        self.posicao = (x, y)
        self.cor_fundo = cor_fundo
    
    def desenhar(self):
        rect = pygame.Rect(self.posicao, self.texto.imagem_texto.get_size())
        pygame.draw.rect(self.tela, self.cor_fundo, rect)
        self.texto.desenhar()
        
    def get_click(self):
        posicao_mouse = pygame.mouse.get_pos()
        rect = pygame.Rect(self.posicao, self.texto.imagem_texto.get_size())

        if rect.collidepoint(posicao_mouse) and pygame.mouse.get_pressed()[0]:
            return True
        
        else:
            return False
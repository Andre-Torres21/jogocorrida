import pygame
from scripts.cone import Cone
from scripts.carro import Carro
from scripts.interfaces import *

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.carro = Carro(tela, 100, 100)
        self.cone = Cone(tela)
        self.estado = 'partida'
        
        self.valor_pontos = 0
        self.contador = 0
        self.texto_pontos = Texto(tela, str(self.valor_pontos), 10, 10, (255, 255, 255), 30)

    def atualizar(self):
        self.estado = 'partida'
        self.carro.atualizar()
        self.cone.atualizar()
        
        self.contador +=1
        if self.contador >= 3600:
            self.valor_pontos += 1
            self.contador = 0
            self.texto_pontos.atualizar_texto(str(self.valor_pontos))
            print(self.valor_pontos)
        self.texto_pontos.desenhar()
        
        if self.cone.detectar_colisao(self.carro.getRect()):
            self.estado = 'menu'
            self.carro.posicao = (100, 100)
            self.cone.x = self.tela.get_width()
            self.valor_pontos = 0
            self.texto_pontos.atualizar_texto(str(self.valor_pontos))
        
        self.carro.desenhar()
        self.cone.desenhar()

        return self.estado
    
class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, 'Jogo de corrida', 100, 20, (255, 255, 255), 40)
        self.estado = 'menu'
        self.botao_jogar = Botao(tela, 'Jogar', 100, 100, 35, (15, 15, 15), (255, 255, 255))
    
    def atualizar(self):
        self.estado = 'menu'
        self.titulo.desenhar()
        self.botao_jogar.desenhar()
        
        if self.botao_jogar.get_click():
            self.estado = 'partida'
        
        return self.estado
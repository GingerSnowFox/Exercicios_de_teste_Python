""" 7-Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta),
toda vez que a tecla espaço for pressionada ou o botão direito for clicado."""
import random
import pygame
from pygame.constants import K_SPACE, KEYDOWN

pygame.init
pygame.font.init()
largura = 1000
altura = 800
tamanho = 50
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quadradinho Amarelo")
amarelo = (253, 253, 150)
cinza = (171, 171, 171)

class Quadrado():
    def __init__(self):
      self.largura = 50
      self.altura = 50
      self.x = random.randint(0, largura-self.largura)
      self.y = random.randint(20, altura-self.altura)
      self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
      self.cor = amarelo
    
    def desenha(self, tela):
      pygame.draw.rect(tela, self.cor, self.area)

lista = []

for i in lista:
    quadrado = Quadrado()
    quadrado.desenha(tela)
    lista.append(quadrado)
out = False

while not out:
    pygame.display.update()
     
    for event in pygame.event.get():
        
        if event.type == KEYDOWN and event.key == K_SPACE:
            quadrado = Quadrado()
            lista.append(quadrado)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            quadrado = Quadrado()
            lista.append(quadrado)
            
        if event.type == pygame.QUIT:
            saiu = True
        tela.fill(cinza)
        
        for i in lista:
            i.desenha(tela)
pygame.quit()

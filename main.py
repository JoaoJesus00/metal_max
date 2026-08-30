import pygame
import sys
import os
from classes.cenario import Cenario
from classes.menu import Menu
from classes.pug import Monty as Pug, ALTURA, VEL

pygame.init()
largura, altura = 1400, 700
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('METAL MAX')
clock = pygame.time.Clock()
dt = 0
BASE = os.path.dirname(os.path.abspath(__file__))
meio_tela = largura // 2
velocidade_jogo = VEL
caminho_cenario = os.path.join(BASE, 'assets', 'imagens', '3.jpg')

cenario = Cenario(caminho_cenario, largura, altura)
menu = Menu(largura, altura)
player = Pug(screen.get_width() / 2, screen.get_height() / 2, BASE)

rodando = True
estado = 'MENU'
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if estado == 'MENU':
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if menu.botao_iniciar.collidepoint(evento.pos):
                    estado = "JOGANDO"
                elif menu.botao_opcoes.collidepoint(evento.pos):
                    estado = "OPCOES"
                elif menu.botao_sair.collidepoint(evento.pos):
                    rodando = False
                
              
    screen.fill((100, 100, 100))
    
    if estado == "MENU":
        menu.desenhar_menu(screen)
    
    elif estado == "JOGANDO":
        keys = pygame.key.get_pressed()
        movimento_fundo = 0
        player.update(keys, dt)
        
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.pos.x < 0:
            player.pos.x =0
                
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.pos.x > meio_tela:
            player.pos.x = meio_tela
            movimento_fundo = velocidade_jogo * dt
        
        cenario.mover(movimento_fundo)
        screen.fill((0, 0, 0))
        cenario.desenhar(screen)
        player.draw(screen)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()
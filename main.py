import pygame
import sys
from classes.cenario import Cenario
from classes.menu import Menu

pygame.init()
largura, altura = 800, 458
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('METAL MAX')
clock = pygame.time.Clock()
dt = 0
velocidade_jogo = 300
meio_tela = largura // 2

cenario = Cenario("assets/imagens/1.jpg", largura, altura)

menu = Menu()


# Soldier 3
sheet3 = pygame.image.load('assets/imagens/soldier3.png').convert_alpha()
sprite = pygame.Rect(0, 0, 35, 35)
sprite_original = sheet3.subsurface(sprite)
sprite_aumentada = pygame.transform.scale_by(sprite_original, 2.5)
player_pos = pygame.Vector2(20, 300)
player_largura = sprite_aumentada.get_width()



rodando = True
estado = 'MENU'
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if estado == "MENU" and evento.type == pygame.MOUSEBUTTONDOWN:
            if menu.botao_iniciar.collidepoint(evento.pos):
                estado = "JOGANDO"
            elif menu.botao_opcoes.collidepoint(evento.pos):
                estado = "OPCOES"
            elif menu.botao_sair.collidepoint(evento.pos):
                rodando = False

    screen.fill((0, 0, 0))
    
    if estado == "MENU":
        menu.desenhar_menu(screen)
    elif estado == "JOGANDO":
        keys = pygame.key.get_pressed()
        movimento_fundo = 0
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            pass # Pular
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            pass # Agaixar
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_pos.x -= velocidade_jogo * dt
            if player_pos.x < 0:
                player_pos.x =0
                
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if player_pos.x < meio_tela:
                player_pos.x += velocidade_jogo * dt
            else:
                player_pos.x = meio_tela
                movimento_fundo = velocidade_jogo * dt
            
        cenario.mover(movimento_fundo)
        screen.fill((0, 0, 0))
        cenario.desenhar(screen)
        screen.blit(sprite_aumentada, player_pos)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()
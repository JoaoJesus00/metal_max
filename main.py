import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('METAL MAX')
clock = pygame.time.Clock()
dt = 0

sheet3 = pygame.image.load('imagens/soldier3.png').convert_alpha()
sprite = pygame.Rect(0, 0, 35, 35)
sprite_original = sheet3.subsurface(sprite)
sprite_aumentada = pygame.transform.scale_by(sprite_original, 3)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# --- Menu ---
fonte = pygame.font.SysFont("Arial", 40)
botao_iniciar = pygame.Rect(300, 180, 220, 60)
botao_opcoes  = pygame.Rect(300, 270, 220, 60)
botao_sair    = pygame.Rect(300, 360, 220, 60)

def desenhar_menu():
    screen.blit(fundo, (0, 0))
    for rect, texto in [(botao_iniciar, "INICIAR"), (botao_opcoes, "OPÇÕES"), (botao_sair, "SAIR")]:
        #cor muda se o mouse estiver sobre o botão
        cor = (80, 80, 80) if rect.collidepoint(pygame.mouse.get_pos()) else (50, 50, 50)
        pygame.draw.rect(screen, cor, rect)
        img = fonte.render(texto, True, (255, 255, 255))
        screen.blit(img, img.get_rect(center=rect.center))

rodando = True
estado = "MENU"
fundo = pygame.image.load("assets/fundo.png").convert()
fundo = pygame.transform.scale(fundo, (800, 600)) 

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        #comeca o menu
        if estado == "MENU" and evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_iniciar.collidepoint(evento.pos):
                estado = "JOGANDO"
            elif botao_opcoes.collidepoint(evento.pos):
                estado = "OPCOES"
            elif botao_sair.collidepoint(evento.pos):
                rodando = False

    if estado == "MENU":
        desenhar_menu()
    elif estado == "JOGANDO":
        screen.fill((100, 100, 100))
        screen.blit(sprite_aumentada, player_pos)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
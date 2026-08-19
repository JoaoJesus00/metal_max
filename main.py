import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('METAL MAX')
clock = pygame.time.Clock()
dt = 0

# Soldier 3
sheet3 = pygame.image.load('imagens/soldier3.png').convert_alpha()
sprite = pygame.Rect(0, 0, 35, 35)
sprite_original = sheet3.subsurface(sprite)
sprite_aumentada = pygame.transform.scale_by(sprite_original, 3)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
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
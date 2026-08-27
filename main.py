import os

import pygame

from classes.soldier import Soldier, ALTURA

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('METAL MAX')
clock = pygame.time.Clock()
dt = 0

BASE = os.path.dirname(os.path.abspath(__file__))

sheet3 = pygame.image.load(os.path.join(BASE, 'imagens', 'soldier3.png')).convert_alpha()
sprite = pygame.Rect(0, 0, 35, 35)
sprite_original = sheet3.subsurface(sprite)
sprite_aumentada = pygame.transform.scale_by(sprite_original, 3)

CEL = 128
ESCALA_MONTY = ALTURA / CEL
monty_sheet = pygame.image.load(os.path.join(BASE, 'imagens', 'char_magenta.png')).convert_alpha()
monty_anims = {
    'Standing': [(0, 0)],
    'Walk':     [(0, c) for c in range(1, 9)],
    'Enter':    [(5, c) for c in range(0, 6)],
    'Jump':     [(9, c) for c in range(0, 8)],
}
monty_frames = {
    nome: [pygame.transform.scale_by(monty_sheet.subsurface(pygame.Rect(c * CEL, l * CEL, CEL, CEL)), ESCALA_MONTY)
           for (l, c) in celulas]
    for nome, celulas in monty_anims.items()
}

player = Soldier(screen.get_width() / 2, screen.get_height() / 2, sprite_aumentada)
personagem = 'soldier'
monty_acao = 'Standing'
monty_frame = 0
monty_tempo = 0


def acao_monty(keys, player):
    if not player.no_chao:
        return 'Jump'
    if keys[pygame.K_w] or keys[pygame.K_s]:
        return 'Enter'
    if keys[pygame.K_a] or keys[pygame.K_d]:
        return 'Walk'
    return 'Standing'


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_2:
            personagem = 'monty' if personagem == 'soldier' else 'soldier'

    keys = pygame.key.get_pressed()
    player.update(keys, dt)

    screen.fill((100, 100, 100))

    if personagem == 'monty':
        nova_acao = acao_monty(keys, player)
        if nova_acao != monty_acao:
            monty_acao = nova_acao
            monty_frame = 0
            monty_tempo = 0
        frames = monty_frames[monty_acao]
        if len(frames) > 1:
            monty_tempo += dt
            if monty_tempo >= 0.1:
                monty_tempo = 0
                monty_frame = (monty_frame + 1) % len(frames)
        surf = frames[monty_frame]
        if player.virado:
            surf = pygame.transform.flip(surf, True, False)
        player.sprite = surf

    player.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

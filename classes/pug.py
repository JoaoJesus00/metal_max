import os
import pygame

VEL = 350
GRAVIDADE = 1000
IMPULSO_PULO = 480
ALTURA = 105
CHAO = 650
CEL = 128
ESCALA_MONTY = ALTURA / CEL


class Monty:
    def __init__(self, x, y, base_path):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2()
        self.hitbox = pygame.Rect(x, y, ALTURA, ALTURA)
        
        self.virado = False
        self.no_chao = False
        self.espaco_anterior = False

        self.acao = 'Standing'
        self.frame_atual = 0
        self.tempo_animacao = 0

        caminho_monty = os.path.join(base_path, 'assets', 'imagens', 'pug.png')
        self.sheet = pygame.image.load(caminho_monty).convert_alpha()

        self.anims_config = {
            'Standing': [(0, 0)],
            'Walk':     [(0, c) for c in range(1, 9)],
            'Enter':    [(5, c) for c in range(0, 6)],
            'Jump':     [(9, c) for c in range(0, 8)],
        }

        self.frames = {
            nome: [
                pygame.transform.scale_by(
                    self.sheet.subsurface(pygame.Rect(c * CEL, l * CEL, CEL, CEL)), 
                    ESCALA_MONTY
                )
                for (l, c) in celulas
            ]
            for nome, celulas in self.anims_config.items()
        }

    def definir_acao(self, keys):
        if not self.no_chao:
            return 'Jump'
        if keys[pygame.K_w]:
            return 'Jump'
        if keys[pygame.K_a] or keys[pygame.K_d]:
            return 'Walk'
        return 'Standing'

    def update(self, keys, dt):
        self.vel.x = (keys[pygame.K_d] - keys[pygame.K_a]) * VEL
        dy_tecla = (keys[pygame.K_s] - keys[pygame.K_w]) * VEL

        if self.vel.x != 0 and dy_tecla != 0:
            self.vel.x *= 0.7071
            dy_tecla *= 0.7071

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and not self.espaco_anterior and self.no_chao:
            self.vel.y = -IMPULSO_PULO
            self.no_chao = False
        self.espaco_anterior = keys[pygame.K_SPACE]

        self.vel.y += GRAVIDADE * dt
        self.pos.x += self.vel.x * dt
        self.pos.y += (dy_tecla + self.vel.y) * dt

        if self.pos.y + ALTURA >= CHAO:
            self.pos.y = CHAO - ALTURA
            self.vel.y = 0
            self.no_chao = True

        self.hitbox.topleft = (round(self.pos.x), round(self.pos.y))

        if self.vel.x > 0:
            self.virado = False
        elif self.vel.x < 0:
            self.virado = True

        nova_acao = self.definir_acao(keys)
        if nova_acao != self.acao:
            self.acao = nova_acao
            self.frame_atual = 0
            self.tempo_animacao = 0

        lista_frames = self.frames[self.acao]
        if len(lista_frames) > 1:
            self.tempo_animacao += dt
            if self.tempo_animacao >= 0.1:
                self.tempo_animacao = 0
                self.frame_atual = (self.frame_atual + 1) % len(lista_frames)

    def draw(self, screen):
        sprite_atual = self.frames[self.acao][self.frame_atual]
        if self.virado:
            sprite_atual = pygame.transform.flip(sprite_atual, True, False)
            
        screen.blit(sprite_atual, self.pos)
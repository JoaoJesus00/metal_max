"""Puggy: o personagem jogavel. Por enquanto anda e da um golpe."""

import pygame

from src import config
from src.entidades.golpe import Golpe


class Puggy:
    """Personagem controlado pelo jogador (WASD para andar, golpe no ataque)."""

    def __init__(self, x, y):
        self.sprite = self._carregar_sprite()
        self.rect = self.sprite.get_rect(center=(x, y))
        self.pos = pygame.Vector2(self.rect.topleft)
        self.direcao = 1  # 1 = direita, -1 = esquerda
        self.golpe = None

    def _carregar_sprite(self):
        try:
            sheet = pygame.image.load(config.IMG_JOGADOR).convert_alpha()
            original = sheet.subsurface(pygame.Rect(0, 0, 35, 35))
            return pygame.transform.scale_by(original, 3)
        except pygame.error as e:
            print(f"[aviso] nao carregou {config.IMG_JOGADOR}: {e}")
            sprite = pygame.Surface((105, 105))
            sprite.fill(config.BRANCO)
            return sprite

    def atualizar(self, dt):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            self.pos.y -= config.VELOCIDADE_JOGADOR * dt
        if teclas[pygame.K_s]:
            self.pos.y += config.VELOCIDADE_JOGADOR * dt
        if teclas[pygame.K_a]:
            self.pos.x -= config.VELOCIDADE_JOGADOR * dt
            self.direcao = -1
        if teclas[pygame.K_d]:
            self.pos.x += config.VELOCIDADE_JOGADOR * dt
            self.direcao = 1
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        if self.golpe:
            self.golpe.atualizar(dt)
            if not self.golpe.ativo:
                self.golpe = None

    def golpear(self):
        """Dispara um golpe se ainda nao houver um ativo."""
        if self.golpe is None:
            self.golpe = Golpe(self.rect, self.direcao)

    def desenhar(self, tela, camera_x=0):
        tela.blit(self.sprite, self.rect.move(-camera_x, 0))
        if self.golpe:
            self.golpe.desenhar(tela, camera_x)

"""Inimigo simples que anda de um lado para o outro."""

import pygame

from src import config


class Inimigo:
    """Inimigo basico. Move na horizontal e pode ser derrotado por um golpe."""

    def __init__(self, x, y, velocidade=100):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.velocidade = velocidade
        self.vivo = True

    def atualizar(self, dt=0):
        if not self.vivo:
            return
        self.rect.x += int(self.velocidade * dt)
        # vai e volta dentro de uma faixa da tela
        if self.rect.x > config.LARGURA - 100 or self.rect.x < 100:
            self.velocidade *= -1

    def desenhar(self, tela, camera_x=0):
        if self.vivo:
            pygame.draw.rect(tela, config.VERMELHO, self.rect.move(-camera_x, 0))

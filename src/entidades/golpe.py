"""Golpe (ataque) do jogador."""

import pygame

from src import config


class Golpe:
    """Ataque do Puggy: um retangulo temporario a frente do personagem.

    Dura alguns frames (timer) e some sozinho. Serve para acertar inimigos.
    """

    DURACAO = 15  # frames que o golpe fica ativo
    LARGURA = 40
    ALTURA = 30

    def __init__(self, rect_jogador, direcao=1):
        # nasce colado a frente do jogador, conforme a direcao (1 dir, -1 esq)
        if direcao >= 0:
            x = rect_jogador.right
        else:
            x = rect_jogador.left - self.LARGURA
        y = rect_jogador.centery - self.ALTURA // 2
        self.rect = pygame.Rect(x, y, self.LARGURA, self.ALTURA)
        self.timer = self.DURACAO
        self.ativo = True

    def atualizar(self, dt=0):
        self.timer -= 1
        if self.timer <= 0:
            self.ativo = False

    def desenhar(self, tela, camera_x=0):
        if self.ativo:
            pygame.draw.rect(tela, config.BRANCO, self.rect.move(-camera_x, 0), 3)

    def acerta(self, alvo):
        """True se o golpe estiver ativo e encostar no rect do alvo."""
        return self.ativo and self.rect.colliderect(alvo.rect)

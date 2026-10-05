"""Obstaculos do cenario: classe base Obstaculo e os tipos Tronco e Fogo."""

import pygame

from src import config


class Obstaculo:
    """Classe base (abstrata) para os obstaculos do jogo.

    Guarda um retangulo de colisao (rect) e se o obstaculo machuca o
    jogador (perigoso). As subclasses devem sobrescrever atualizar e
    desenhar.
    """

    def __init__(self, x, y, largura, altura, perigoso=False):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.perigoso = perigoso

    def atualizar(self, dt=0):
        raise NotImplementedError("Subclasse deve implementar atualizar()")

    def desenhar(self, tela, camera_x=0):
        raise NotImplementedError("Subclasse deve implementar desenhar()")


class Tronco(Obstaculo):
    """Tronco parado no caminho. Nao machuca, apenas bloqueia."""

    def __init__(self, x, y):
        super().__init__(x, y, 90, 40, perigoso=False)

    def atualizar(self, dt=0):
        pass  # tronco e estatico

    def desenhar(self, tela, camera_x=0):
        pygame.draw.rect(tela, config.MARROM, self.rect.move(-camera_x, 0))


class Fogo(Obstaculo):
    """Fogo animado. E perigoso e oscila para simular a chama."""

    def __init__(self, x, y):
        super().__init__(x, y, 40, 50, perigoso=True)
        self.contador = 0

    def atualizar(self, dt=0):
        self.contador = (self.contador + 1) % 60

    def desenhar(self, tela, camera_x=0):
        oscila = 10 if self.contador < 30 else 0
        r = self.rect.move(-camera_x, -oscila)
        r.height += oscila
        pygame.draw.rect(tela, config.LARANJA, r)

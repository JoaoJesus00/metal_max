"""Menu inicial: botoes Iniciar, Opcoes e Sair."""

import pygame

from src import config


class Menu:
    """Desenha o menu e informa qual botao foi clicado."""

    def __init__(self, tela, fundo):
        self.tela = tela
        self.fundo = fundo
        self.fonte = pygame.font.SysFont("Arial", 40)
        cx = config.LARGURA // 2 - 110
        self.botoes = {
            "INICIAR": pygame.Rect(cx, 180, 220, 60),
            "OPCOES": pygame.Rect(cx, 270, 220, 60),
            "SAIR": pygame.Rect(cx, 360, 220, 60),
        }
        self.rotulos = {"INICIAR": "INICIAR", "OPCOES": "OPÇÕES", "SAIR": "SAIR"}

    def desenhar(self):
        self.tela.blit(self.fundo, (0, 0))
        for chave, rect in self.botoes.items():
            hover = rect.collidepoint(pygame.mouse.get_pos())
            cor = config.BOTAO_HOVER if hover else config.BOTAO
            pygame.draw.rect(self.tela, cor, rect)
            img = self.fonte.render(self.rotulos[chave], True, config.BRANCO)
            self.tela.blit(img, img.get_rect(center=rect.center))

    def clique(self, pos):
        """Retorna a chave do botao clicado ('INICIAR'/'OPCOES'/'SAIR') ou None."""
        for chave, rect in self.botoes.items():
            if rect.collidepoint(pos):
                return chave
        return None

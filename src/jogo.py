"""Classe Jogo: orquestra o loop principal e os estados (MENU/JOGANDO/OPCOES)."""

import pygame

from src import config
from src.ui.menu import Menu
from src.entidades.puggy import Puggy
from src.entidades.inimigo import Inimigo
from src.entidades.obstaculos import Tronco, Fogo


class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((config.LARGURA, config.ALTURA))
        pygame.display.set_caption(config.TITULO)
        self.clock = pygame.time.Clock()
        self.rodando = True
        self.estado = config.MENU

        # Fundo carregado ANTES de quem o usa (corrige a ordem de definicao).
        self.fundo = self._carregar_fundo()
        self.menu = Menu(self.tela, self.fundo)
        self.fonte = pygame.font.SysFont("Arial", 30)

        # Entidades da partida (criadas ao clicar em INICIAR).
        self.puggy = None
        self.inimigo = None
        self.obstaculos = []

    def _carregar_fundo(self):
        """Carrega o fundo com tratamento de erro (nao quebra se o arquivo faltar)."""
        try:
            img = pygame.image.load(config.IMG_FUNDO).convert()
            return pygame.transform.scale(img, (config.LARGURA, config.ALTURA))
        except pygame.error as e:
            print(f"[aviso] nao carregou {config.IMG_FUNDO}: {e}")
            fundo = pygame.Surface((config.LARGURA, config.ALTURA))
            fundo.fill(config.CINZA_FUNDO)
            return fundo

    def _iniciar_partida(self):
        self.puggy = Puggy(config.LARGURA // 2, config.ALTURA // 2)
        self.inimigo = Inimigo(600, 300)
        self.obstaculos = [Tronco(150, 400), Fogo(400, 150)]

    def _eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

            if self.estado == config.MENU and evento.type == pygame.MOUSEBUTTONDOWN:
                escolha = self.menu.clique(evento.pos)
                if escolha == "INICIAR":
                    self._iniciar_partida()
                    self.estado = config.JOGANDO
                elif escolha == "OPCOES":
                    self.estado = config.OPCOES
                elif escolha == "SAIR":
                    self.rodando = False

            elif self.estado == config.OPCOES and evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # volta ao menu
                    self.estado = config.MENU

            elif self.estado == config.JOGANDO and evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    self.puggy.golpear()
                elif evento.key == pygame.K_ESCAPE:
                    self.estado = config.MENU

    def _atualizar(self, dt):
        if self.estado == config.JOGANDO:
            self.puggy.atualizar(dt)
            self.inimigo.atualizar(dt)
            for obstaculo in self.obstaculos:
                obstaculo.atualizar(dt)
            # golpe do Puggy derrota o inimigo
            if self.puggy.golpe and self.inimigo.vivo:
                if self.puggy.golpe.acerta(self.inimigo):
                    self.inimigo.vivo = False

    def _desenhar(self):
        if self.estado == config.MENU:
            self.menu.desenhar()
        elif self.estado == config.OPCOES:
            self._desenhar_opcoes()
        elif self.estado == config.JOGANDO:
            self.tela.fill(config.CINZA_FUNDO)
            for obstaculo in self.obstaculos:
                obstaculo.desenhar(self.tela)
            self.inimigo.desenhar(self.tela)
            self.puggy.desenhar(self.tela)
        pygame.display.flip()

    def _desenhar_opcoes(self):
        """Tela de opcoes (placeholder) com retorno ao menu — corrige o beco sem saida."""
        self.tela.fill(config.BOTAO)
        linhas = ["OPCOES", "", "(em construcao)", "ESC para voltar"]
        y = 200
        for linha in linhas:
            img = self.fonte.render(linha, True, config.BRANCO)
            self.tela.blit(img, img.get_rect(center=(config.LARGURA // 2, y)))
            y += 50

    def rodar(self):
        dt = 0
        while self.rodando:
            self._eventos()
            self._atualizar(dt)
            self._desenhar()
            dt = self.clock.tick(config.FPS) / 1000
        pygame.quit()

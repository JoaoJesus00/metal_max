import pygame

class Cenario:
    def __init__(self, caminho_imagem, largura, altura):
        self.imagem = pygame.image.load(caminho_imagem).convert()
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
        self.largura_imagem = self.imagem.get_width()
        self.x = 0
        
    def mover(self, deslocamento):
        self.x -= deslocamento
        
        if self.x <= -self.largura_imagem:
            self.x = 0
            
        if self.x > 0:
            self.x = -self.largura_imagem + self.x
            
    def desenhar(self, superficie):
        superficie.blit(self.imagem, (self.x, 0))
        superficie.blit(self.imagem, (self.x + self.largura_imagem, 0)  )
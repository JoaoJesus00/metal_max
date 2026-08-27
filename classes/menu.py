import pygame

class Menu:
    def __init__(self):
        self.fonte = pygame.font.SysFont(None, 40)
        self.botao_iniciar = pygame.Rect(300, 110, 220, 60)
        self.botao_opcoes  = pygame.Rect(300, 200, 220, 60)
        self.botao_sair    = pygame.Rect(300, 290, 220, 60)
        self.fundo = pygame.image.load("assets/imagens/fundo.png").convert()
        self.fundo_t = pygame.transform.scale(self.fundo, (800, 600)) 
        
    def desenhar_menu(self, screen):
        screen.blit(self.fundo, (0, 0))
        for rect, texto in [(self.botao_iniciar, "INICIAR"), (self.botao_opcoes, "OPÇÕES"), (self.botao_sair, "SAIR")]:
            #cor muda se o mouse estiver sobre o botão
            cor = (80, 80, 80) if rect.collidepoint(pygame.mouse.get_pos()) else (50, 50, 50)
            pygame.draw.rect(screen, cor, rect)
            img = self.fonte.render(texto, True, (255, 255, 255))
            screen.blit(img, img.get_rect(center=rect.center))
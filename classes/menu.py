import pygame

class Menu:
    def __init__(self, largura, altura):
        self.fonte = pygame.font.SysFont(None, 40)
        largura_btn = 220
        altura_btn = 60
        espaco = 30
        pos_x = (largura - largura_btn) // 2
        num_botoes = 3
        altura_total_grupo = (num_botoes * altura_btn) + ((num_botoes - 1) * espaco)
        pos_y_inicial = (altura - altura_total_grupo) // 2
        self.botao_iniciar = pygame.Rect(pos_x, pos_y_inicial, largura_btn, altura_btn)
        self.botao_opcoes  = pygame.Rect(pos_x, pos_y_inicial + (altura_btn + espaco), largura_btn, altura_btn)
        self.botao_sair    = pygame.Rect(pos_x, pos_y_inicial + (altura_btn + espaco) * 2, largura_btn, altura_btn)
        self.fundo = pygame.image.load("assets/imagens/fundo.png").convert()
        self.fundo_t = pygame.transform.scale(self.fundo, (largura, altura)) 
        
    def desenhar_menu(self, screen):
        screen.blit(self.fundo_t, (0, 0))
        for rect, texto in [(self.botao_iniciar, "INICIAR"), (self.botao_opcoes, "OPÇÕES"), (self.botao_sair, "SAIR")]:
            #cor muda se o mouse estiver sobre o botão
            cor = (80, 80, 80) if rect.collidepoint(pygame.mouse.get_pos()) else (50, 50, 50)
            pygame.draw.rect(screen, cor, rect)
            img = self.fonte.render(texto, True, (255, 255, 255))
            screen.blit(img, img.get_rect(center=rect.center))
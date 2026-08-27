import pygame

VEL = 300
GRAVIDADE = 1000
IMPULSO_PULO = 480
ALTURA = 105
CHAO = 560


class Soldier:
    def __init__(self, x, y, sprite):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2()
        self.sprite = sprite
        self.hitbox = pygame.Rect(x, y, ALTURA, ALTURA)
        self.virado = False
        self.no_chao = False
        self.espaco_anterior = False

    def update(self, keys, dt):
        self.vel.x = (keys[pygame.K_d] - keys[pygame.K_a]) * VEL
        dy_tecla = (keys[pygame.K_s] - keys[pygame.K_w]) * VEL
        if self.vel.x != 0 and dy_tecla != 0:
            self.vel.x *= 0.7071
            dy_tecla *= 0.7071

        if keys[pygame.K_SPACE] and not self.espaco_anterior and self.no_chao:
            self.vel.y = -IMPULSO_PULO
            self.no_chao = False
        self.espaco_anterior = keys[pygame.K_SPACE]

        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.vel.y = 0
        else:
            self.vel.y += GRAVIDADE * dt

        self.pos.x += self.vel.x * dt
        self.pos.y += (dy_tecla + self.vel.y) * dt
        if self.vel.x > 0:
            self.virado = False
        elif self.vel.x < 0:
            self.virado = True

        if self.pos.y + ALTURA >= CHAO:
            self.pos.y = CHAO - ALTURA
            self.vel.y = 0
            self.no_chao = True

        self.hitbox.topleft = (round(self.pos.x), round(self.pos.y))

    def draw(self, screen):
        screen.blit(self.sprite, self.pos)

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Classe para gerenciar as balas disparadas pelo foguete."""

    def __init__(self, screen, rocket):
        """Cria uma bala na posição atual do foguete."""
        super().__init__()
        self.screen = screen

        # Cria um retângulo da bala
        self.rect = pygame.Rect(0, 0, 15, 3)  # largura, altura
        self.rect.centery = rocket.rect.centery
        self.rect.left = rocket.rect.right

        # Armazena a posição horizontal como float para movimento suave
        self.x = float(self.rect.x)

        self.color = (255, 0, 0)
        self.speed = 10

    def update(self):
        """Move a bala para a direita na tela."""
        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Desenha a bala na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)

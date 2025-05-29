import pygame
import os


class Rocket:
    def __init__(self, screen):
        """Inicializa o foguete e define sua posição inicial."""
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Carrega a imagem do foguete
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "images/rocket.png")
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_image, (50, 75))  # largura, altura

        # Pega o retângulo da imagem e da tela
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Começa o foguete no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha o foguete na tela na posição atual."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Atualiza a posição do foguete se estiver se movendo para a direita."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 10
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 10
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 10
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 10

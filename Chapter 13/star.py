import pygame
import os


class Star(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen

        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "images", "star.png")
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_image, (40, 40))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)

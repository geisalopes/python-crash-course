import pygame
import os
from star import Star
from random import randint

# Inicializa o pygame
pygame.init()

# Tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Stars Grid")

# Relógio
clock = pygame.time.Clock()

# Grupo de sprites
stars = pygame.sprite.Group()

# Tamanho e espaçamento
star_width = 40
star_height = 40
spacing_x = 60
spacing_y = 60

# Número de linhas e colunas
num_cols = 12
num_rows = 8

# Calcular tamanho total da grade
grid_width = num_cols * spacing_x
grid_height = num_rows * spacing_y

# Margens para centralizar
margin_x = (800 - grid_width) // 2
margin_y = (600 - grid_height) // 2

# Criar estrelas com pequenas variações aleatórias
for row in range(num_rows):
    for col in range(num_cols):
        x = margin_x + col * spacing_x + randint(-10, 10)
        y = margin_y + row * spacing_y + randint(-10, 10)

        star = Star(screen, x, y)
        stars.add(star)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 20))  # Fundo escuro

    for star in stars:
        star.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

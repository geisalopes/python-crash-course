import pygame
from rocket import Rocket

from bullet import Bullet
import pygame.sprite

# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rocket Game")

# Cria um relógio para controlar os frames por segundo
clock = pygame.time.Clock()

# Cria o foguete
rocket = Rocket(screen)

# Cria as balas
bullets = pygame.sprite.Group()

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, rocket)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

    rocket.update()
    bullets.update()

    # Remove as balas da tela
    for bullet in bullets.copy():
        if bullet.rect.left > screen.get_rect().right:
            bullets.remove(bullet)

    # Preenche a tela com uma cor
    screen.fill((255, 253, 208))

    # Desenha o foguete
    rocket.blitme()

    for bullet in bullets:
        bullet.draw_bullet()

    # Atualiza a tela
    pygame.display.flip()

    # Limita para 60 FPS
    clock.tick(60)  # limits FPS to 60

pygame.quit()

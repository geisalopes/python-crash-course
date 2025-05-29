import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a janela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Teclas pressionadas")

# Define a fonte e a cor do texto
font = pygame.font.SysFont(None, 72)
text_color = (0, 0, 0)  # preto
bg_color = (255, 253, 208)  # amarelo manteiga :)

# Mensagem padrão
key_text = ""

# Loop principal
while True:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Atualiza o texto com o nome da tecla
            key_text = pygame.key.name(event.key)

    # Renderiza o texto na tela
    text_image = font.render(key_text, True, text_color, bg_color)
    text_rect = text_image.get_rect(center=screen.get_rect().center)
    screen.blit(text_image, text_rect)

    pygame.display.flip()

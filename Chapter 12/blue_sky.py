import sys
import pygame

from screen import Screen
from dragon import Dragon


class BlueSky:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Screen()
        self.screen = pygame.display.set_mode(
            (self.settings.tela_width, self.settings.tela_height)
        )
        pygame.display.set_caption("Blue Sky")
        self.dragon = Dragon(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.dragon.blitme()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()

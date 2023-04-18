import pygame
from level import Level


class Renderer:
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        self._level.all_sprites.draw(self._display)

        #Draw score
        font = pygame.font.SysFont("Arial", 36)
        score_text = font.render("Score: " + str(Level.get_score(self._level)), True, (255, 255, 255))
        self._display.blit(score_text, (5, 10))

        #Draw game over
        if not Level.get_player(self._level).alive():
            font = pygame.font.SysFont("Arial", 36)
            score_text = font.render("Game Over!", True, (255, 255, 255))
            self._display.blit(score_text, (160, 10))

        pygame.display.update()

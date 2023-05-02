import pygame
from level import Level


class Renderer:
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        self._level.all_sprites.draw(self._display)

        # Draw score
        font = pygame.font.SysFont("Arial", 36)
        score_text = font.render(
            "Score: " + str(Level.get_score(self._level)), True, (255, 255, 255))
        self._display.blit(score_text, (5, 10))

        if Level.get_lives(self._level) > 0:
            score_text = font.render(
                "Lives: " + str(Level.get_lives(self._level)), True, (255, 255, 255))
            self._display.blit(score_text, (160, 10))

        score_text = font.render(
            "Level: " + str(Level.get_level(self._level)), True, (255, 255, 255))
        self._display.blit(score_text, (460, 10))

        if Level.get_powerup_status(self._level):
            score_text = font.render(
                "Power up activated for 5 seconds!", True, (255, 255, 255))
            self._display.blit(score_text, (140, 620))
        # Draw game over
        if not Level.get_player(self._level).alive():
            self._display.fill((0, 0, 0))
            score_text = font.render(
                "Game Over! Press 'e' to go back to the main menu", True, (255, 255, 255))
            self._display.blit(score_text, (30, 300))

        pygame.display.update()

import pygame
from level import Level


class Renderer:
    """Luokka, jolla piirretään pelitapahtumat näytölle
    """
    def __init__(self, display, level):
        """Luokan konstruktori, joka luo piirtäjän

        Args:
            display (pygame.display): Näyttö jolle tapahtumat piirretään
            level (Level): Pelikenttä, joka piirretään
        """
        self._display = display
        self._level = level

    def render(self):
        """Piirretään tapahtumat, sekä tekstit näytölle ja lopuksi päivitetään näyttö
        """
        self._level.all_sprites.draw(self._display)

        font = pygame.font.SysFont("Arial", 36)
        score_text = font.render(
            "Score: " + str(Level.get_score(self._level)), True, (255, 255, 255))
        self._display.blit(score_text, (5, 10))

        if Level.get_lives(self._level) > 0:
            score_text = font.render(
                "Lives: " + str(Level.get_lives(self._level)), True, (255, 255, 255))
            self._display.blit(score_text, (300, 10))

        score_text = font.render(
            "Level: " + str(Level.get_level(self._level)), True, (255, 255, 255))
        self._display.blit(score_text, (500, 10))

        if Level.get_powerup_status(self._level):
            score_text = font.render(
                "Power up activated for 5 seconds!", True, (255, 255, 255))
            self._display.blit(score_text, (140, 620))

        if not Level.get_player(self._level).alive():
            self._display.fill((0, 0, 0))
            gameover_text = font.render("Game over!", True, (255, 255, 255))
            score_text = font.render(
                "Press 'e' to submit your score", True, (255, 255, 255))
            self._display.blit(gameover_text, (240, 200))
            self._display.blit(score_text, (140, 300))

        pygame.display.update()

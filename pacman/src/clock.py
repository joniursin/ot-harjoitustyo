import pygame


class Clock:
    """Luokka, jota käytetään pelin kellona
    """
    def __init__(self):
        """Luokan konstruktori, joka luo kellon
        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Pitää huolen, että peli kulkee tietyllä fps määrällä

        Args:
            fps (int): Pelin fps määrä
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """Palauttaa kuluneen ajan käynnistyksestä

        Returns:
            int: Kulunut aika käynnistyksestä
        """
        return pygame.time.get_ticks()

import pygame


class EventQueue:
    """Luokka, joka pitää huolen pelin tapahtumista
    """
    def get(self):
        """Palauttaa pelaajan näppäinpainalmukset

        Returns:
            pygame.event: Palauttaa tapahtumat
        """
        return pygame.event.get()

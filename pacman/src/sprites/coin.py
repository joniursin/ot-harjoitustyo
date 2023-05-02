import os
import pygame

dirname = os.path.dirname(__file__)


class Coin(pygame.sprite.Sprite):
    """Luokka, joka luo kolikko olion

    Args:
        pygame (pygame.sprite): Luo sprite olion
    """

    def __init__(self, x_coord=0, y_coord=0):
        """Luokan konstruktori, joka luo oliolle paikan pelikentällä

        Args:
            x_coord (int, optional): Maailman x-koordinaatti. Defaults to 0.
            y_coord (int, optional): Maailman y-koordinaatti. Defaults to 0.
        """
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "coin.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord

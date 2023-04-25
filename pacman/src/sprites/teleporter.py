import os
import pygame

dirname = os.path.dirname(__file__)


class Teleporter(pygame.sprite.Sprite):
    def __init__(self, x_coord=0, y_coord=0, direction=""):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "floor.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.direction = direction

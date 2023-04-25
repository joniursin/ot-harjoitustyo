import os
import random
import pygame

dirname = os.path.dirname(__file__)


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x_coord=0, y_coord=0):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "ghost.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.direction = random.choice(["N", "S", "W", "E"])

    def move(self, cell_size):
        if self.direction == "N":
            self.rect.move_ip(0, -cell_size)
        elif self.direction == "S":
            self.rect.move_ip(0, cell_size)
        elif self.direction == "E":
            self.rect.move_ip(cell_size, 0)
        else:
            self.rect.move_ip(-cell_size, 0)

    def check_move(self, cell_size, boxes):
        exits = []

        self.rect.move_ip(cell_size, 0)
        if not pygame.sprite.spritecollide(self, boxes, False):
            exits.append("E")
        self.rect.move_ip(-cell_size, 0)

        self.rect.move_ip(-cell_size, 0)
        if not pygame.sprite.spritecollide(self, boxes, False):
            exits.append("W")
        self.rect.move_ip(cell_size, 0)

        self.rect.move_ip(0, cell_size)
        if not pygame.sprite.spritecollide(self, boxes, False):
            exits.append("S")
        self.rect.move_ip(0, -cell_size)

        self.rect.move_ip(0, -cell_size)
        if not pygame.sprite.spritecollide(self, boxes, False):
            exits.append("N")
        self.rect.move_ip(0, cell_size)

        return exits

    def choose_move(self, cell_size, boxes):
        exits = self.check_move(cell_size, boxes)
        if self.direction in exits and random.randrange(0, 100) <= 50:
            pass
        else:
            self.direction = random.choice(exits)
        self.move(cell_size)

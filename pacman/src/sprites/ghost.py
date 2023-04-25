import os
import pygame
import random

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

    def move(self, CELL_SIZE):
        if self.direction == "N":
            self.rect.move_ip(0, -CELL_SIZE)
        elif self.direction == "S":
            self.rect.move_ip(0, CELL_SIZE)
        elif self.direction == "E":
            self.rect.move_ip(CELL_SIZE, 0)
        else:
            self.rect.move_ip(-CELL_SIZE, 0)

    def check_move(self, CELL_SIZE, boxes):
        exits = []

        self.rect.move_ip(CELL_SIZE, 0)
        if not pygame.sprite.spritecollide(self, boxes, False):
            exits.append("E")
        self.rect.move_ip(-CELL_SIZE, 0)

        self.rect.move_ip(-CELL_SIZE, 0)
        if not pygame.sprite.spritecollide(self, boxes, False):
            exits.append("W")
        self.rect.move_ip(CELL_SIZE, 0)

        self.rect.move_ip(0, CELL_SIZE)
        if not pygame.sprite.spritecollide(self, boxes, False):
            exits.append("S")
        self.rect.move_ip(0, -CELL_SIZE)

        self.rect.move_ip(0, -CELL_SIZE)
        if not pygame.sprite.spritecollide(self, boxes, False):
            exits.append("N")
        self.rect.move_ip(0, CELL_SIZE)

        return exits
    
    def choose_move(self, CELL_SIZE, boxes):
        exits = self.check_move(CELL_SIZE, boxes)
        if self.direction in exits and random.randrange(0, 100) <= 50:
            pass
        else:
            self.direction = random.choice(exits)
        self.move(CELL_SIZE)
        

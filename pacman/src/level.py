import pygame
from sprites.player import Player
from sprites.box import Box
from sprites.floor import Floor
from sprites.coin import Coin


class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.player = None
        self.boxes = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.boxes.add(Box(normalized_x, normalized_y))
                elif cell == 2:
                    self.player = Player(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 3:
                    self.coins.add(Coin(normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(self.floors, self.boxes, self.coins, self.player)

    def _check_move(self, x=0, y=0):
        self.player.rect.move_ip(x, y)
        colliding_walls = pygame.sprite.spritecollide(
            self.player, self.boxes, False)
        can_move = not colliding_walls

        self.player.rect.move_ip(-x, -y)
        return can_move

    def move_player(self, x=0, y=0):
        if not self._check_move(x, y):
            return

        self.player.rect.move_ip(x, y)

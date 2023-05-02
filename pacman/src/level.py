import random
import pygame
from sprites.player import Player
from sprites.box import Box
from sprites.floor import Floor
from sprites.coin import Coin
from sprites.ghost import Ghost
from sprites.teleporter import Teleporter
from sprites.powerup import PowerUp


class Level:
    def __init__(self, level_map, cell_size, clock):
        self.clock = clock
        self.score = 0
        self.lives = 3
        self.level = 1
        self.level_map = level_map
        self.cell_size = cell_size
        self.width = len(level_map[0])
        self.player = None
        self.powerup_active = False
        self.teleporter_left = None
        self.teleporter_right = None
        self.boxes = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.time_left = None

        self._initialize_sprites(self.level_map)

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y_coord in range(height):
            for x_coord in range(width):
                cell = level_map[y_coord][x_coord]
                normalized_x = x_coord * self.cell_size
                normalized_y = y_coord * self.cell_size

                if cell == 0:
                    if random.randrange(0, 100) <= 55:
                        self.coins.add(Coin(normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.boxes.add(Box(normalized_x, normalized_y))
                elif cell == 2:
                    self.player = Player(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 3:
                    self.coins.add(Coin(normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 4:
                    self.ghosts.add(Ghost(normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 5:
                    self.teleporter_left = Teleporter(
                        normalized_x, normalized_y, "left")
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 6:
                    self.teleporter_right = Teleporter(
                        normalized_x, normalized_y, "right")
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 7:
                    self.powerups.add(PowerUp(normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(self.floors, self.boxes,
                             self.coins, self.powerups, self.player, self.ghosts)

    def check_death(self):
        death = pygame.sprite.spritecollide(self.player, self.ghosts, False)
        if pygame.sprite.spritecollide(self.player, self.ghosts, False) and not self.powerup_active:
            self.lives -= 1
            if self.lives > 0:
                self.boxes = pygame.sprite.Group()
                self.floors = pygame.sprite.Group()
                self.coins = pygame.sprite.Group()
                self.ghosts = pygame.sprite.Group()
                self.all_sprites = pygame.sprite.Group()
                self._initialize_sprites(self.level_map)
            else:
                self.player.kill()

        if pygame.sprite.spritecollide(self.player, self.ghosts, False) and self.powerup_active:
            pygame.sprite.spritecollide(self.player, self.ghosts, True)

        return death

    def _check_move(self, x_coord=0, y_coord=0):
        self.player.rect.move_ip(x_coord, y_coord)
        can_move = False
        if pygame.sprite.spritecollide(self.player, self.floors, False):
            colliding_walls = pygame.sprite.spritecollide(
                self.player, self.boxes, False)
            can_move = not colliding_walls

        self.player.rect.move_ip(-x_coord, -y_coord)
        return can_move

    def _check_collect_coin(self):
        if pygame.sprite.spritecollide(self.player, self.coins, True):
            self.score += 1

    def _activate_powerup(self):
        self.time_left = self.clock.get_ticks() + 5000
        self.powerup_active = True

    def check_powerup(self):
        if pygame.sprite.spritecollide(self.player, self.powerups, True):
            self._activate_powerup()
        if self.time_left is None:
            return
        if self.time_left < self.clock.get_ticks():
            self.powerup_active = False

    def move_player(self, x_coord=0, y_coord=0):
        if not self._check_move(x_coord, y_coord) or not self.player.alive():
            return
        self.player.rect.move_ip(x_coord, y_coord)
        # if pygame.sprite.collide_rect(self.player, self.teleporter_left):
        # self.player.rect.move_ip(self.cell_size*(self.width-1), y_coord)
        # elif pygame.sprite.collide_rect(self.player, self.teleporter_right):
        # self.player.rect.move_ip(-(self.cell_size*(self.width-1)), y_coord)

        self._check_collect_coin()

    def get_score(self):
        return self.score

    def get_player(self):
        return self.player

    def move_ghosts(self):
        for ghost in self.ghosts:
            ghost.choose_move(self.cell_size, self.boxes)

    def get_lives(self):
        return self.lives

    def set_lives(self, value):
        self.lives = value

    def get_level(self):
        return self.level

    def get_powerup_status(self):
        return self.powerup_active

    def check_coins(self):
        if not self.coins:
            # no coins on map = new level
            self.level += 1
            self.boxes = pygame.sprite.Group()
            self.floors = pygame.sprite.Group()
            self.coins = pygame.sprite.Group()
            self.ghosts = pygame.sprite.Group()
            self.all_sprites = pygame.sprite.Group()
            self._initialize_sprites(self.level_map)

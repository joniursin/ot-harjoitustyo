import random
import pygame
from sprites.player import Player
from sprites.box import Box
from sprites.floor import Floor
from sprites.coin import Coin
from sprites.ghost import Ghost
from sprites.powerup import PowerUp


class Level:
    """Luokka, joka luo tason ja tutkii sen tapahtumia
    """
    def __init__(self, level_map, cell_size, clock):
        """Luokan konstruktori, joka luo uuden tason

        Args:
            level_map (list): Tason kuvaelma
            cell_size (int): Yhden kentän neliön koko
            clock (Clock): Pelin kello
        """
        self.clock = clock
        self.score = 0
        self.lives = 3
        self.level = 1
        self.level_map = level_map
        self.cell_size = cell_size
        self.width = len(level_map[0])
        self.player = None
        self.powerup_active = False
        self.boxes = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.time_left = None

        self._initialize_sprites(self.level_map)

    def _initialize_sprites(self, level_map):
        """Tekee jokaisesta taso neliöstä spriten ja lisää sille koordinaatit pelissä

        Args:
            level_map (list): Tason kuvaelma
        """
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
                elif cell == 7:
                    self.powerups.add(PowerUp(normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(self.floors, self.boxes,
                             self.coins, self.powerups, self.player, self.ghosts)

    def check_death(self):
        """Tarkistaa onko pelaaja osunut kummitukseen, jos on vähenetään elämä

        Returns:
            bool: Palauttaa True, jos pelaaja on kuollut ja False jos ei
        """
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
            death = False
            self.score += 400 * self.level
            pygame.sprite.spritecollide(self.player, self.ghosts, True)

        return death

    def _check_move(self, x_coord=0, y_coord=0):
        """Tarkistaa voiko pelaaja liikkua eli onko seinä edessä

        Args:
            x_coord (int, optional): Maailman x-koordinaatti. Defaults to 0.
            y_coord (int, optional): Maailman y-koordinaatti. Defaults to 0.

        Returns:
            bool: True, jos voi liikkua muuten False
        """
        self.player.rect.move_ip(x_coord, y_coord)
        can_move = False
        if pygame.sprite.spritecollide(self.player, self.floors, False):
            colliding_walls = pygame.sprite.spritecollide(
                self.player, self.boxes, False)
            can_move = not colliding_walls

        self.player.rect.move_ip(-x_coord, -y_coord)
        return can_move

    def _check_collect_coin(self):
        """Tarkistaa onko pelaaja kolikon päällä ja kerää tämän
        """
        if pygame.sprite.spritecollide(self.player, self.coins, True):
            self.score += 10 * self.level

    def _activate_powerup(self):
        """Aktivoi power upin 
        """
        self.time_left = self.clock.get_ticks() + 5000
        self.powerup_active = True

    def check_powerup(self):
        """Tarkistaa onko pelaaja power upin kohdalla, jos on kutsuu sen käynnistystä
        """
        if pygame.sprite.spritecollide(self.player, self.powerups, True):
            self.score += 100 * self.level
            self._activate_powerup()
        if self.time_left is None:
            return
        if self.time_left < self.clock.get_ticks():
            self.powerup_active = False

    def move_player(self, x_coord=0, y_coord=0):
        """Liikuttaa pelaajaa kyseiseen kohtaan

        Args:
            x_coord (int, optional): Maailman x-koordinaatti. Defaults to 0.
            y_coord (int, optional): Maailman y-koordinaatti. Defaults to 0.
        """
        if not self._check_move(x_coord, y_coord) or not self.player.alive():
            return
        self.player.rect.move_ip(x_coord, y_coord)

        self._check_collect_coin()

    def get_score(self):
        """Palauttaa scoren

        Returns:
            int: Pelaajan score
        """
        return self.score

    def get_player(self):
        """Palauttaa pelaajan

        Returns:
            Player: Pelaaja olio
        """
        return self.player

    def move_ghosts(self):
        """Liikuttaa kummituksia kentällä
        """
        for ghost in self.ghosts:
            ghost.choose_move(self.cell_size, self.boxes)

    def get_lives(self):
        """Palauttaa elämät

        Returns:
            int: Pelaajan elämät
        """
        return self.lives

    def set_lives(self, value):
        """Asettaa elämät tietyksi

        Args:
            value (int): Elämien määrä
        """
        self.lives = value

    def get_level(self):
        """Palauttaa tason numeron

        Returns:
            int : Taso
        """
        return self.level

    def get_powerup_status(self):
        """Palauttaa onko power up aktiivinen

        Returns:
            bool : power upin tila
        """
        return self.powerup_active

    def check_coins(self):
        """Tarkistaa onko kentällä enää kolikoita tai power uppeja, jos ei luo uuden tason
        """
        if not self.coins and not self.powerups:
            self.level += 1
            self.boxes = pygame.sprite.Group()
            self.floors = pygame.sprite.Group()
            self.coins = pygame.sprite.Group()
            self.ghosts = pygame.sprite.Group()
            self.all_sprites = pygame.sprite.Group()
            self._initialize_sprites(self.level_map)

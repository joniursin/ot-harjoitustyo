import pygame
import database_connection
from level import Level
from datetime import datetime

class GameLoop:
    """Luokka, joka vastaa pelistä, sen ajankulusta sekä tapahtumista
    """
    def __init__(self, level, renderer, event_queue, clock, cell_size, player_name):
        """Luokan konstruktori, joka luo pelin

        Args:
            level (Level): Peli kenttä
            renderer (Renderer): Piirtäjä
            event_queue (EventQueue): Tapahtumajono
            clock (Clock): Pelin kello
            cell_size (int): Yhden kentän neliön koko
            player_name (string): Pelaajan nimi
        """
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._ghost_movement = self._clock.get_ticks() + 1000
        self._player_name = player_name
        self._connection = database_connection.get_database_connection()

    def start(self):
        """Aloittaa pelin kulun
        """
        while True:
            if self._handle_events() is False:
                break
            self._render()
            self._clock.tick(60)

    def _handle_events(self):
        """Käsittelee pelin tapahtumat, kuten näppäimen painalmukset sekä lataa uuden tason

        Returns:
            False: Palauttaa False, kun peli on päättynyt
        """
        if self._level.check_death():
            self._ghost_movement = self._clock.get_ticks() + 2000

        # load new level
        self._level.check_coins()

        # activate power up if collected and deactivates when time runs out
        self._level.check_powerup()

        if self._clock.get_ticks() > self._ghost_movement:
            self._level.move_ghosts()
            self._ghost_movement += 500

        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_player(x_coord=-self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self._level.move_player(x_coord=self._cell_size)
                if event.key == pygame.K_UP:
                    self._level.move_player(y_coord=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self._level.move_player(y_coord=self._cell_size)
                if event.key == pygame.K_e and self._level.check_death():
                    # After death submit score via sqlite
                    date = datetime.now()
                    date = date.strftime("%d/%m/%Y %H:%M:%S")

                    cursor = self._connection.cursor()
                    cursor.execute("INSERT INTO scores (player, score, date) VALUES (?, ?, ?);", (self._player_name, Level.get_score(self._level), date))

                    return False
            elif event.type == pygame.QUIT:
                pygame.quit()
                break

    def _render(self):
        """Kutsuu piirtäjää piirtämään ruudun tapahtumat
        """
        self._renderer.render()

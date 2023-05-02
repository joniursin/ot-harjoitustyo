import pygame


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._ghost_movement = self._clock.get_ticks() + 1000

    def start(self):
        while True:
            if self._handle_events() is False:
                break
            self._render()
            self._clock.tick(60)

    def _handle_events(self):
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
                    return False
            elif event.type == pygame.QUIT:
                pygame.quit()

    def _render(self):
        self._renderer.render()

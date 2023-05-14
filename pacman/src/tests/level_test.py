import unittest
from level import Level
from clock import Clock

LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 4, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 2, 0, 7, 4, 0, 0, 0, 0, 1],
             [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50
CLOCK = Clock()


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP, CELL_SIZE, CLOCK)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_player_cant_move_through_walls(self):
        player = self.level.player

        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.level.move_player(x_coord=-CELL_SIZE)
        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.level.move_player(x_coord=CELL_SIZE)
        self.assert_coordinates_equal(player, 2 * CELL_SIZE, 2 * CELL_SIZE)

    def test_player_can_collect_coins(self):
        player = self.level.player

        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.assertEqual(self.level.score, 0)

        self.level.move_player(y_coord=CELL_SIZE)
        self.assertEqual(self.level.score, 10)

        self.level.move_player(y_coord=CELL_SIZE)
        self.assertEqual(self.level.score, 20)

    def test_player_can_die(self):
        player = self.level.player

        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.level.set_lives(1)
        self.level.move_player(y_coord=-CELL_SIZE)

        self.level.check_death()
        self.assertEqual(self.level.player.alive(), False)

    def test_losing_lives(self):
        player = self.level.player

        self.assertEqual(self.level.get_lives(), 3)

        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.level.move_player(y_coord=-CELL_SIZE)
        self.level.check_death()
        self.assertEqual(self.level.get_lives(), 2)

    def test_powerup_pickup(self):

        player = self.level.player

        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.assertEqual(self.level.get_powerup_status(), False)

        self.level.move_player(x_coord=CELL_SIZE)
        self.level.check_powerup()
        self.assertEqual(self.level.get_powerup_status(), False)

        self.level.move_player(x_coord=CELL_SIZE)
        self.level.check_powerup()
        self.assertEqual(self.level.get_powerup_status(), True)

    def test_powerup_kills_enemies(self):

        player = self.level.player

        self.assertEqual(self.level.get_lives(), 3)

        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.assertEqual(self.level.get_powerup_status(), False)

        self.level.move_player(x_coord=CELL_SIZE)
        self.level.move_player(x_coord=CELL_SIZE)
        self.level.check_powerup()
        self.assertEqual(self.level.get_powerup_status(), True)

        self.level.move_player(x_coord=CELL_SIZE)
        self.level.check_death()
        self.assertEqual(self.level.get_lives(), 3)

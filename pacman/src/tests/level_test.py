import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 4, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP, CELL_SIZE)

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
        self.assertEqual(self.level.score, 1)

        self.level.move_player(y_coord=CELL_SIZE)
        self.assertEqual(self.level.score, 2)

    def test_player_can_die(self):
        player = self.level.player

        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.level.move_player(y_coord=-CELL_SIZE)
        self.level.check_death()
        self.assertEqual(self.level.player.alive(), False)


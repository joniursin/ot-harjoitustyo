import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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

        self.level.move_player(x=-CELL_SIZE)
        self.assert_coordinates_equal(player, CELL_SIZE, 2 * CELL_SIZE)

        self.level.move_player(x=CELL_SIZE)
        self.assert_coordinates_equal(player, 2 * CELL_SIZE, 2 * CELL_SIZE)

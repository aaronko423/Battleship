import unittest
from app.gameboard import GameBoard


class TestBoard(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_grid_created(self):
        g = GameBoard()
        self.assertIsInstance(g.grid, list, "grid property is a list")

    def test_letter_from_comparison(self):
        g = GameBoard()
        x_input = g.x_ran
        y_input = g.y_ran
        g.input(x_input, y_input)
        self.assertTrue(g.grid[x_input][y_input]==["X"], "returns X if equal to random numbers")

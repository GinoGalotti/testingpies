import unittest
import pytest
from game_of_life import GameLife


class GetSum(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    def test_a_round_runs(self):
        life = GameLife()
        self.assertTrue(life.round())

    def test_run_9999_rounds(self):
        life = GameLife()
        for i in range(9999):
            self.assertTrue(life.round())

    # Add tests with given scenarios
    def test_two_by_two_resurrects(self):
        board = [   [ 1, 1],
                    [ 1, 0]]
        game = GameLife(board)

        self.assertTrue(game.round())

        after_board = [ [ 1, 1],
                        [ 1, 1]]
        self.assertEqual(after_board, game.board)

    def test_two_by_two_stays_kills_both(self):
        board = [   [ 1, 0],
                    [ 1, 0]]
        game = GameLife(board)

        self.assertTrue(game.round())

        after_board = [ [ 0, 0],
                        [ 0, 0]]
        self.assertEqual(after_board, game.board)
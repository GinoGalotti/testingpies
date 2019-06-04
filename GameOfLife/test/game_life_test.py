import unittest

from game_of_life import GameLife


class GetSum(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    @classmethod
    def setup_class(cls):
        cls.life = GameLife()

    def test_a_round_runs(self):
        self.assertTrue(self.life.round())

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
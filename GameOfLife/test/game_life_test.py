import unittest
import time
from game_of_life import GameLife


class GetSum(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > 0.3:
            print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

    def test_a_round_runs(self):
        life = GameLife()
        self.assertTrue(life.round())

    def test_run_9999_rounds(self):
        started = time.time()
        life = GameLife()
        for i in range(9999):
            self.assertTrue(life.round())

        self.assertLess(round(time.time() - started,2),2)

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
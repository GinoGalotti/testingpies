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
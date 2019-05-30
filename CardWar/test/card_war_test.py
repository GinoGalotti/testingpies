import unittest

from card_war import CardGame


class CardWardTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    def test_two_equal(self):
        self.assertEqual(recurring_character.recurring_character('AA'), 'A')

    def test_two_equal_and_jump(self):
        self.assertEqual(recurring_character.recurring_character('ABAB'), 'A')

    def test_no_duplicate(self):
        self.assertEqual(recurring_character.recurring_character('AB'), '')

    def test_empty_string(self):
        self.assertEqual(recurring_character.recurring_character(''), '')

    def test_long_string(self):
        self.assertEqual(
            recurring_character.recurring_character('ACIDECALE'), 'C')

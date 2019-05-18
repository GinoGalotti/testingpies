import unittest

import sum_of_numbers


class GetSum(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    def test_sum_two(self):
        self.assertEqual(sum_of_numbers.get_sum(1, 2), 3)

    def test_sum_two_negative(self):
        self.assertEqual(sum_of_numbers.get_sum(-1, -2), -3)

    def test_sum_three(self):
        self.assertEqual(sum_of_numbers.get_sum(1, 3), 6)

    def test_equal(self):
        self.assertEqual(sum_of_numbers.get_sum(3, 3), 3)

    def test_equal_negative(self):
        self.assertEqual(sum_of_numbers.get_sum(-3, -3), -3)

    def test_negative_and_positive(self):
        self.assertEqual(sum_of_numbers.get_sum(-2, 10), -
                         2-1+0+1+2+3+4+5+6+7+8+9+10)

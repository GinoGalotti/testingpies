import unittest

import base_ten
from functools import reduce


class BaseTen(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    def test_000_plus_one(self):
        self.assertEqual(base_ten.add_one([0, 0, 0]), [0, 0, 1])

    def test_999_plus_one(self):
        self.assertEqual(base_ten.add_one([9, 9, 9]), [1, 0, 0, 0])

    def test_many_numbers(self):
        self.assertEqual(base_ten.add_one([0, 3, 0]), [0, 3, 1])
        self.assertEqual(base_ten.add_one([1, 0, 9]), [1, 1, 0])
        self.assertEqual(base_ten.add_one([2, 9, 9]), [3, 0, 0])
        self.assertEqual(base_ten.add_one([2, 3, 5]), [2, 3, 6])

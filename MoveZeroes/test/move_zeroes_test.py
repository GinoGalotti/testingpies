import unittest

import move_zeroes


class MoveZeroes(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    def test_only_zero(self):
        self.assertEqual(move_zeroes.move([0]), [0])

    def test_only_zeroes(self):
        self.assertEqual(move_zeroes.move([0, 0]), [0, 0])

    def test_one_and_zero(self):
        self.assertEqual(move_zeroes.move([0, 1]), [1, 0])

    def test_no_zero(self):
        self.assertEqual(move_zeroes.move([True, 2, 1, "yes"]), [True, 2, 1, "yes"])
    
    # False is treated as 0 in some List methods
    def test_no_zero_but_false(self):
        self.assertEqual(move_zeroes.move([False, 2, 1, "yes"]), [False, 2, 1, "yes"])


    ## This is planning to be an exhaustive testing suite

    def test_zero_and_false(self):
        self.assertEqual(move_zeroes.move([0, False, 0, 2, 0, 1, "yes"]), [False, 2, 1, "yes", 0, 0, 0])
    
    def test_zero_as_string(self):
        self.assertEqual(move_zeroes.move([0, False, "0", 2, 0, 1, "yes"]), [False, "0", 2, 1, "yes", 0, 0])

    def test_double_zero(self):
        self.assertEqual(move_zeroes.move([0, False, 00 , 2, 0, 1, "yes"]), [False, 2, 1, "yes", 0, 0, 0])



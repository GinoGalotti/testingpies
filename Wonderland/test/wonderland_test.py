import unittest

import wonderland_number

class WonderlandTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    def test_nested_loop(self):
        self.assertEqual("142857", wonderland_number.find_number_list_nested_loop())

    def test_same_numbers(self):
        self.assertTrue(wonderland_number.same_digits([1,1,0,0,1,0], [0,1,0,1,0,1]))
        self.assertTrue(wonderland_number.same_digits([1,2,3,4,5,6], [6,5,4,3,2,1]))

    def test_multiply_list(self):
        self.assertEqual([2,2,2,2,2,2], wonderland_number.multiply_and_return_list([1,1,1,1,1,1], 2))

        self.assertEqual([1,0,2,4,3,8], wonderland_number.multiply_and_return_list([0,5,1,2,1,9], 2))
        self.assertEqual([0,5,6,0,9,5], wonderland_number.multiply_and_return_list([0,1,1,2,1,9], 5))
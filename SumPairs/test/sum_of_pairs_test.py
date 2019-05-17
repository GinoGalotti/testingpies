import unittest

import sum_of_pairs


class GetSum(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    def test_sum_two(self):
        self.assertEqual(sum_of_pairs.find_pair([1,2], 3), [1,2])
    
    def test_sum_return_shortest(self):
        self.assertEqual(sum_of_pairs.find_pair([1,2,2,3], 4), [2,2])

    # This should work
    def test_sum_return_duplicates(self):
        self.assertEqual(sum_of_pairs.find_pair([1,2,1,4,3,3,2], 4), [1,3])


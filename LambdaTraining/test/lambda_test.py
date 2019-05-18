import unittest

import lambda_training
from functools import reduce


class TestingLambda(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    def test_plus_plus(self):
        self.assertEqual(lambda_training.plus_plus(3), 4)

        plus_plus = lambda x: x + 1
        self.assertEqual(plus_plus(3), 4)

    def test_lambda_on_map_list(self):    
        list1 = [1,2,3,4,5]
        list1 = list(map(lambda x: x + 1, list1))

        self.assertEqual(list1,[2,3,4,5,6])

    def test_lambda_on_filter_list(self):
        list1 = [1,2,3,4,5]
        list1 = list(filter(lambda x: x < 3, list1))

        self.assertEqual(list1, [1,2])

        list2 = [1, 2, 3, None, True, "Yeah", "Aham"]
        list2 = list(filter(lambda x: isinstance(x, str), list2))

        self.assertEqual(list2, ["Yeah", "Aham"])

    def test_lambda_on_reduce_list(self):
        list1 = [1,2,3,4,5]
        list1 = reduce(lambda x, y: x * y, list1)

        self.assertEqual(list1, 1*2*3*4*5)

        list2 = [1, 2, 3, None, "Yeah", "Aham"]
        list2 = reduce(lambda x, y: x - y, list(filter(lambda x: isinstance(x, int), list2)))

        self.assertEqual(list2, 1-2-3)




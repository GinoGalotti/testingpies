import unittest

import binary_search


class IterativeTests(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata http://pythontesting.net/framework/pytest/pytest-xunit-style-fixtures/
    """

    def test_search_empty(self):
        self.assertEqual(-1, binary_search.search_iterative(3, []))

    def test_search_out_of_boundary(self):
        self.assertEqual(-1, binary_search.search_iterative(3, [1]))

        self.assertEqual(-1, binary_search.search_iterative(0, [1, 3, 5]))
        self.assertEqual(-1, binary_search.search_iterative(6, [1, 3, 5]))

        self.assertEqual(-1, binary_search.search_iterative(0, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_search.search_iterative(8, [1, 3, 5, 7]))

    def test_find_in_two(self):
        self.assertEqual(0, binary_search.search_iterative(1, [1, 3]))

    def test_find_in_three(self):
        self.assertEqual(0, binary_search.search_iterative(1, [1, 3, 5]))
        self.assertEqual(1, binary_search.search_iterative(3, [1, 3, 5]))
        self.assertEqual(2, binary_search.search_iterative(5, [1, 3, 5]))

    def test_find_in_four(self):
        self.assertEqual(0, binary_search.search_iterative(1, [1, 3, 5, 7]))
        self.assertEqual(1, binary_search.search_iterative(3, [1, 3, 5, 7]))
        self.assertEqual(2, binary_search.search_iterative(5, [1, 3, 5, 7]))
        self.assertEqual(3, binary_search.search_iterative(7, [1, 3, 5, 7]))

    def test_missing_in_between(self):
        self.assertEqual(-1, binary_search.search_iterative(2, [1, 3, 5]))
        self.assertEqual(-1, binary_search.search_iterative(4, [1, 3, 5]))

        self.assertEqual(-1, binary_search.search_iterative(2, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_search.search_iterative(4, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_search.search_iterative(6, [1, 3, 5, 7]))

class RecursiveTests(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata http://pythontesting.net/framework/pytest/pytest-xunit-style-fixtures/
    """

    def test_search_empty(self):
        self.assertEqual(-1, binary_search.search_recursive(3, []))

    def test_search_out_of_boundary(self):
        self.assertEqual(-1, binary_search.search_recursive(3, [1]))

        self.assertEqual(-1, binary_search.search_recursive(0, [1, 3, 5]))
        self.assertEqual(-1, binary_search.search_recursive(6, [1, 3, 5]))

        self.assertEqual(-1, binary_search.search_recursive(0, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_search.search_recursive(8, [1, 3, 5, 7]))

    def test_find_in_two(self):
        self.assertEqual(0, binary_search.search_recursive(1, [1, 3]))

    def test_find_in_three(self):
        self.assertEqual(0, binary_search.search_recursive(1, [1, 3, 5]))
        self.assertEqual(1, binary_search.search_recursive(3, [1, 3, 5]))
        self.assertEqual(2, binary_search.search_recursive(5, [1, 3, 5]))

    def test_find_in_four(self):
        self.assertEqual(0, binary_search.search_recursive(1, [1, 3, 5, 7]))
        self.assertEqual(1, binary_search.search_recursive(3, [1, 3, 5, 7]))
        self.assertEqual(2, binary_search.search_recursive(5, [1, 3, 5, 7]))
        self.assertEqual(3, binary_search.search_recursive(7, [1, 3, 5, 7]))

    def test_missing_in_between(self):
        self.assertEqual(-1, binary_search.search_recursive(2, [1, 3, 5]))
        self.assertEqual(-1, binary_search.search_recursive(4, [1, 3, 5]))

        self.assertEqual(-1, binary_search.search_recursive(2, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_search.search_recursive(4, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_search.search_recursive(6, [1, 3, 5, 7]))


class LongTests(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        ones = [1] * 999999
        twos = [2] * 999999
        threes = [3] * 999999
        fours = [4] * 999999
        fives = [5] * 999999
        sixs = [6] * 999999
        cls.long_array = list([0]+ones+twos+threes+fours+fives+sixs)

    def test_long_one_python(self):
        self.assertEqual(0, binary_search.search_python(0, self.long_array))

    # Several times worst than the python implementation
    def test_long_one_iterative(self):
        self.assertEqual(0, binary_search.search_iterative(0, self.long_array))

    def test_long_one_recursive(self):
        self.assertEqual(0, binary_search.search_recursive(0, self.long_array))

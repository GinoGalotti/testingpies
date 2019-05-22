import unittest

import binary_search


class BinaryTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    def test_search_empty(self):
        self.assertEqual(-1, binary_search.search_iterative(3,[]))
    
    def test_search_out_of_boundary(self):
        self.assertEqual(-1, binary_search.search_iterative(3,[1]))

        self.assertEqual(-1, binary_search.search_iterative(0,[1,3,5]))
        self.assertEqual(-1, binary_search.search_iterative(6,[1,3,5]))

        self.assertEqual(-1, binary_search.search_iterative(0,[1,3,5,7]))
        self.assertEqual(-1, binary_search.search_iterative(8,[1,3,5,7]))
        
    def test_find_in_two(self):
        self.assertEqual(0, binary_search.search_iterative(1,[1,3]))

    def test_find_in_three(self):
        self.assertEqual(0, binary_search.search_iterative(1,[1,3,5]))
        self.assertEqual(1, binary_search.search_iterative(3,[1,3,5]))
        self.assertEqual(2, binary_search.search_iterative(5,[1,3,5]))

    def test_find_in_four(self):
        self.assertEqual(0, binary_search.search_iterative(1,[1,3,5,7]))
        self.assertEqual(1, binary_search.search_iterative(3,[1,3,5,7]))
        self.assertEqual(2, binary_search.search_iterative(5,[1,3,5,7]))
        self.assertEqual(3, binary_search.search_iterative(7,[1,3,5,7]))
    
    # def test_missing_in_between(self):
    #     self.assertEqual(-1, binary_search.search_iterative(2,[1,3,5]))
    #     self.assertEqual(-1, binary_search.search_iterative(4,[1,3,5]))

    #     self.assertEqual(-1, binary_search.search_iterative(2,[1,3,5,7]))
    #     self.assertEqual(-1, binary_search.search_iterative(4,[1,3,5,7]))
    #     self.assertEqual(-1, binary_search.search_iterative(6,[1,3,5,7]))

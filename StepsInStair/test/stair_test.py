import unittest

from step_stairs import Stair


class StairTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    def test_one_step_works(self):
        stair = Stair(5)
        self.assertEqual(stair.num_ways([1]), 1)
    
    def test_five_steps_works(self):
        stair = Stair(5)
        self.assertEqual(stair.num_ways([5]), 1)

    def test_no_solution_available(self):
        stair = Stair(5)
        self.assertEqual(stair.num_ways([2]), 0)

    def test_two_ways(self):
        stair = Stair(5)
        self.assertEqual(stair.num_ways([2,1]), 8)

    def test_three_ways_one_doesnt_work(self):
        stair = Stair(5)
        self.assertEqual(stair.num_ways([1,2,6]), 8)

    def test_repeated_number_doesnt_count(self):
        stair = Stair(5)
        self.assertEqual(stair.num_ways([2,1,1]), 8)

    # def test_big_number_for_performance(self):
    #     stair = Stair(100)
    #     self.assertEqual(stair.num_ways([3,5,7,10,2,9]), 100)
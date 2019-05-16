import unittest

from Kata import Kata

class KataTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    def test_true(self):
        kata = Kata()

        self.assertTrue(kata.return_true())
        self.assertFalse(kata.return_true(), "this is an excepted error")
        assert kata.return_true()


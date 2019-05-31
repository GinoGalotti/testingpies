import unittest

from cypher import Cypher


class CodeTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    @classmethod
    def setup_class(cls):
        cls.cypher = Cypher()

    def test_a_to_find_keys(self):
        self.assertEqual("scones", self.cypher.encode("aaaaaa"))

    def test_use_keys_longer_than_the_key(self):
        self.assertEqual("sconessc", self.cypher.encode("aaaaaaaa"))

    def test_one_letter(self):
        self.assertEqual("u", self.cypher.encode("c"))

    def test_with_new_key(self):
        self.cypher.set_key("vigilance")
        self.assertEqual("hmkbxebpxpmyllyrxiiqtoltfgzzv", self.cypher.encode("meetmeontuesdayeveningatseven"))

class DecipherTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    @classmethod
    def setup_class(cls):
        cls.cypher = Cypher()

    def test_a_to_find_keys(self):
        self.assertEqual("scones", self.cypher.decipher("packmyboxwithfivedozenliquorjugs", "hcqxqqtqljmlzhwiivgbsapaiwcenmyu"))
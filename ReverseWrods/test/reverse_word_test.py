import unittest

import reverse_words


class ReverseWord(unittest.TestCase):

    def test_one_word_equals(self):
        self.assertEqual(reverse_words.reverse("hi"), "hi")

    def test_one_word_trailing_deleted(self):
        self.assertEqual(reverse_words.reverse("hi "), "hi")

    def test_two_words(self):
        self.assertEqual(reverse_words.reverse("hi darling"), "darling hi")

    def test_two_words_trailspace(self):
        self.assertEqual(reverse_words.reverse("hi darling "), "darling hi")
        self.assertEqual(reverse_words.reverse(" hi darling "), "darling hi")
        self.assertEqual(reverse_words.reverse(" hi darling"), "darling hi")

    def test_three_words(self):
        self.assertEqual(reverse_words.reverse(
            "hi! darling home"), "home darling hi!")

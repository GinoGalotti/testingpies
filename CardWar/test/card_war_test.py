import unittest

from card_war import CardGame, CardType, CardValue, Card


class CardWardUnitTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Fail with one number

    @classmethod
    def setup_class(cls):
        cls.card_game = CardGame()
        cls.card_game.init_game()

    # Test setup works
    def test_initial_deck(self):
        self.assertEqual(26, len(self.card_game.player1_deck))
        self.assertEqual(26, len(self.card_game.player2_deck))

        # TODO: Check that we have one of each card

    # Test internal methods
    def test_ace_better_than_king(self):
        self.assertEqual(1, self.card_game.wins(Card(CardType.Clubs, CardValue.Ace), Card(CardType.Diamonds, CardValue.King)))
        self.assertEqual(2, self.card_game.wins(Card(CardType.Diamonds, CardValue.King), Card(CardType.Clubs, CardValue.Ace)))

    def test_jack_better_than_ten(self):
        self.assertEqual(1, self.card_game.wins(Card(CardType.Clubs, CardValue.Jack), Card(CardType.Diamonds, CardValue.Ten)))
        self.assertEqual(2, self.card_game.wins(Card(CardType.Diamonds, CardValue.Ten), Card(CardType.Clubs, CardValue.Jack)))
    
    def test_tie_when_same_value(self):
        self.assertEqual(0, self.card_game.wins(Card(CardType.Clubs, CardValue.Ace), Card(CardType.Diamonds, CardValue.Ace)))
        self.assertEqual(0, self.card_game.wins(Card(CardType.Diamonds, CardValue.Jack), Card(CardType.Clubs, CardValue.Jack)))

    def test_is_end_game_is_0_when_both_have_decks(self):
        self.assertEqual(0, self.card_game.is_end_game())
    
    def test_is_end_game_returns_correctly_when_one_is_empty(self):
        new_game = CardGame()
        new_deck = [Card(CardType.Clubs, CardValue.Ace), Card(CardType.Diamonds, CardValue.Ace)]

        new_game.set_decks([], new_deck)
        self.assertEqual(2, new_game.is_end_game())

        new_game.set_decks(new_deck, [])
        self.assertEqual(1, new_game.is_end_game())

    def test_is_end_game_returns_correctly_when_both_are_empty(self):
        new_game = CardGame()

        new_game.set_decks([], [])
        self.assertEqual(3, new_game.is_end_game())

class CardWardPlayingTest(unittest.TestCase):
    """
    Seems to not be able to use a BeforeAll to initiate the Kata
    """

    # Test setup works
    def test_playing_works(self):
        card_game = CardGame()
        card_game.init_game()
        
        self.assertNotEqual(0, card_game.game())

    def test_play_first_card_win(self):
        card_game = CardGame()
        deck1 = [Card(CardType.Clubs, CardValue.Ace), Card(CardType.Diamonds, CardValue.Ace)]
        deck2 = [Card(CardType.Clubs, CardValue.Queen), Card(CardType.Diamonds, CardValue.Queen)]
        card_game.set_decks(deck1, deck2)

        card_game.play()

        self.assertEqual(3, len(card_game.player1_deck))
        self.assertEqual(1, len(card_game.player2_deck))

    def test_play_second_card_win(self):
        card_game = CardGame()
        deck1 = [Card(CardType.Clubs, CardValue.Ace), Card(CardType.Diamonds, CardValue.Ace), Card(CardType.Hearts, CardValue.Ace), Card(CardType.Spades, CardValue.Ace), Card(CardType.Spades, CardValue.King), Card(CardType.Spades, CardValue.Queen)]
        deck2 = [Card(CardType.Clubs, CardValue.Ace), Card(CardType.Diamonds, CardValue.Queen), Card(CardType.Hearts, CardValue.Queen), Card(CardType.Spades, CardValue.Queen), Card(CardType.Spades, CardValue.Three), Card(CardType.Spades, CardValue.Two)]
        card_game.set_decks(deck1, deck2)

        card_game.play()

        self.assertEqual(11, len(card_game.player1_deck))
        self.assertEqual(1, len(card_game.player2_deck))

    def test_loses_after_a_play(self):
        card_game = CardGame()
        deck1 = [Card(CardType.Clubs, CardValue.Ace)]
        deck2 = [Card(CardType.Clubs, CardValue.Queen)]
        card_game.set_decks(deck1, deck2)

        card_game.play()
        
        self.assertEqual(2, len(card_game.player1_deck))
        self.assertEqual(0, len(card_game.player2_deck))
        self.assertEqual(1, card_game.is_end_game())
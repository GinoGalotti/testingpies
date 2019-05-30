# Info and definition on https://github.com/gigasquid/wonderland-clojure-katas/tree/master/card-game-war

from collections import namedtuple
from random import shuffle

class CardType:
    Spades = 0
    Hearts = 1
    Diamonds = 2
    Clubs = 3

class CardValue:
    Ace = 14
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

class CardGame:

    def __init__(self):
        self.card = namedtuple("Card", "Value Type")
        types = [CardType.Spades, CardType.Diamonds, CardType.Clubs, CardType.Hearts]
        values = [CardValue.Ace, CardValue.Two, CardValue.Three, CardValue.Four, CardValue.Five, CardValue.Six, 
            CardValue.Seven, CardValue.Eight, CardValue.Nine, CardValue.Ten, CardValue.Jack, CardValue.Queen, CardValue.King]
        deck = []
        for card_type in types:
            for card_value in values:
                deck.append(self.card(card_value, card_type))
        shuffle(deck)

        self.player1_deck = deck[:26]
        self.player2_deck = deck[26:]


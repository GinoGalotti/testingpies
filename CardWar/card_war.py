# Info and definition on https://github.com/gigasquid/wonderland-clojure-katas/tree/master/card-game-war

# TODO: Fix the playing game

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

Card = namedtuple("Card", "Type Value")

class CardGame:

    def init_game(self):
        types = [CardType.Spades, CardType.Diamonds, CardType.Clubs, CardType.Hearts]
        values = [CardValue.Ace, CardValue.Two, CardValue.Three, CardValue.Four, CardValue.Five, CardValue.Six, 
            CardValue.Seven, CardValue.Eight, CardValue.Nine, CardValue.Ten, CardValue.Jack, CardValue.Queen, CardValue.King]
        deck = []
        for card_type in types:
            for card_value in values:
                deck.append(Card(card_type, card_value))
        shuffle(deck)

        self.player1_deck = deck[:26]
        self.player2_deck = deck[26:]
        self.cards_at_play = []

    def play(self):
        print("I'm playing " + str(self.player1_deck) +"+"+ str(self.player2_deck))
        card1 = self.player1_deck.pop(0)
        card2 = self.player2_deck.pop(0)
        self.cards_at_play.extend([card1, card2])

        result = self.wins(card1,card2)
        print("Result is {0}".format(str(result)))

        if result == 1:
            self.player1_deck.extend(self.cards_at_play)
            self.cards_at_play.clear()
            print("Player 1 should win with {0}".format(str(self.player1_deck)))
            return 1
        
        elif result == 2:
            self.player2_deck.extend(self.cards_at_play)
            self.cards_at_play.clear()
            return 2
        
        else:
            if self.is_end_game() == 0:
                # Put 3 cards on the pile and play again
                self.cards_at_play.append([self.player1_deck.pop(0)])
                self.cards_at_play.append([self.player2_deck.pop(0)])
                if self.is_end_game() != 0 :
                    return 0
                
                self.cards_at_play.append([self.player1_deck.pop(0)])
                self.cards_at_play.append([self.player2_deck.pop(0)])
                if self.is_end_game() != 0:
                    return 0

                self.cards_at_play.append([self.player1_deck.pop(0)])
                self.cards_at_play.append([self.player2_deck.pop(0)])
                if self.is_end_game() != 0:
                    return 0

                return self.play()
            else:
                return 0
        # Recursion, having a variable where you put the "bet"

    def game(self):
        winner = 0
        while winner == 0:
            self.play()
            winner = self.is_end_game()
        return winner

    # 1 wins player 1, 2 wins player 2, 0 keep playing, 3 both ran out of cards at the same time
    def is_end_game(self):
        print(str(self.player1_deck) +"+"+ str(self.player2_deck))

        if self.player1_deck == [] and self.player2_deck == []:
            return 3
        if self.player1_deck == []:
            return 2
        elif self.player2_deck == []:
            return 1
        return 0

    # For testing purposes
    def set_decks(self, deck1, deck2):
        self.player1_deck = deck1
        self.player2_deck = deck2
        self.cards_at_play = []
    
    # Returns 0 when they are the same, 1 when the first one wins, 2 when the second one
    def wins(self, card1, card2):
        difference = card1.Value - card2.Value

        if difference == 0:
            return 0
        if difference < 0: 
            return 2
        else:
            return 1
        
        #TODO: Make option where Type matters and they have an entire deck each
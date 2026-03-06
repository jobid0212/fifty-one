import random

from card import Card
from suits import Suits
from values import Values


class Deck:
    def __init__(self, size: int) -> None:
        """
        Initializes a deck of cards based on size. size 1 = 52 cards. size 2 = 104 cards
        """
        deck = []

        for suit in Suits:
            if suit != Suits.JOKER:
                for value in Values:
                    for i in range(0, size):
                        deck.append(Card(suit, value))

        for i in range(0, size):
            deck.append(Card(Suits.JOKER, Values.ACE))

        self.deck = deck

    def __str__(self) -> str:
        cards = ""
        for card in self.deck:
            cards += str(card)
            cards += ", "

        return cards

    def shuffle_deck(self) -> None:
        random.shuffle(self.deck)


a = Deck(2)
a.shuffle_deck()
print(a)

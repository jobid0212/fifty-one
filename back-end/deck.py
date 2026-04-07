import random

from card import Card
from suits import Suits
from values import Values


class Deck:
    """
    Functionality for the main decks (draw pile and played cards).
    """

    def __init__(self) -> None:
        self.deck = []

    def __str__(self) -> str:
        cards = ""
        for card in self.deck:
            cards += str(card)
            cards += ", "

        return cards

    def make_full_deck(self) -> None:
        """
        Creates a base deck with all 106 cards (includes 2 jokers).
        """

        for i in range(2):
            self.deck.append(Card(Suits.JOKER, Values.ACE))

            for suit in Suits:
                if suit != Suits.JOKER:
                    for value in Values:
                        self.deck.append(Card(suit, value))

    def shuffle_deck(self) -> None:
        random.shuffle(self.deck)

    def remove_card(self) -> Card:
        try:
            return self.deck.pop()
        except IndexError:
            raise IndexError("No cards to remove")

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

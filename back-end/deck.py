from suits import Suits
from values import Values
from card import initialize_card
import random

"""
    Initializes a deck of cards based on size. size 1 = 52 cards. size 2 = 104 cards
"""
def initialize_deck(size: int) -> list:
    deck = []

    for suit in Suits:
        if suit != Suits.JOKER:
            for value in Values:
                for i in range(0, size):
                    deck.append(initialize_card(suit, value))

    for i in range(0, size):
        deck.append(initialize_card(Suits.JOKER, Values.ACE))
    
    return deck

def shuffle_deck(deck: list) -> None:
    random.shuffle(deck)

a = initialize_deck(2)
shuffle_deck(a)
print(a)
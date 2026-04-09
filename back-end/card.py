from functools import total_ordering

from suits import Suits
from values import Values


@total_ordering
class Card:
    def __init__(self, suit: Suits, value: Values) -> None:
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        if self.value != other.value:
            return self.value.value < other.value.value

        return self.suit.value < other.suit.value

    def __str__(self) -> str:
        if self.suit == Suits.JOKER:
            return "Joker"
        else:
            return f"{self.value.name.lower()} of {self.suit.name.lower()}"

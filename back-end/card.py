from suits import Suits
from values import Values


class Card:
    def __init__(self, suit: Suits, value: Values) -> None:
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        if self.suit == Suits.JOKER:
            return "Joker"
        else:
            return f"{self.value.name.lower()} of {self.suit.name.lower()}"

from suits import Suits
from values import Values

def initialize_card(suit: Suits, value: Values) -> dict:
    card = {
        "suit" : suit,
        "value" : value
    }
    return card


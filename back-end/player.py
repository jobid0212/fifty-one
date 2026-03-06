from card import Card

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
    
    def add_card_to_hand(self, card: Card):
        self.hand.append(card)

    def remove_card_from_hand(self, card: Card): # removing specific card object
        self.hand.remove(card)

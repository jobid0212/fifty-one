from card import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.prev_winner = False
        self.opened = False

    def __str__(self) -> str:
        s = f"{self.name}'s hand: \n"
        for i, card in enumerate(self.hand):
            s += str(i + 1) + ".) " + str(card) + "\n"
        return s

    def add_card_to_hand(self, card: Card) -> None:
        if len(self.hand) > 15:
            raise ValueError("Cannot have more than 15 cards in a hand.")

        self.hand.append(card)

    def remove_card_from_hand(self, card: Card) -> None:
        try:
            self.hand.remove(card)
        except ValueError:
            raise ValueError("Cannot remove from hand when player has no cards")

    def play_turn(self):
        print(self)

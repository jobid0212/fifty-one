from deck import Deck
from player import Player


class Game:
    def __init__(self, players: list, previous_winner: Player) -> None:
        if len(players) > 7 or len(players) < 2:
            raise ValueError("Invalid player count.")

        self.players = players
        self.current_player = previous_winner  # Take prev winner as a param and init it to be the first `current_player`

        self.play_deck = Deck()
        self.play_deck.make_full_deck()
        self.play_deck.shuffle_deck()

        self.discard_pile = Deck()

    def deal_cards(self) -> None:  # Maybe change logic in case we want an animation?
        for player in self.players:
            if player == self.current_player:
                player.append(self.play_deck.remove_card())

            for _ in range(14):
                player.append(self.play_deck.remove_card())

    def play(self) -> Player | None:
        self.deal_cards()

        return None

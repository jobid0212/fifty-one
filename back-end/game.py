from card import Card
from deck import Deck
from player import Player
from suits import Suits
from values import Values


class Game:
    def __init__(self, players: list, previous_winner: Player) -> None:
        if len(players) > 7 or len(players) < 2:
            raise ValueError("Invalid player count.")

        self.current_player = previous_winner  # Take prev winner as a param and init it to be the first `current_player`

        self.play_deck = Deck()
        self.play_deck.make_full_deck()
        self.play_deck.shuffle_deck()

        self.discard_pile = Deck()

        self.players = players
        self.last_discarded = Card(Suits.SPADES, Values.ACE)
        self.top_of_play_deck = self.play_deck.deck[-1]

    def deal_cards(self) -> None:  # Maybe change logic in case we want an animation?
        for player in self.players:
            if player == self.current_player:
                player.hand.append(self.play_deck.remove_card())

            for _ in range(14):
                player.hand.append(self.play_deck.remove_card())

    def query_for_replay(self) -> bool:
        unanswered = True
        while unanswered:
            try:
                user_input = input("Do you want to play again? (Y/n) ")

                # Validate input
                if not user_input.isalpha():
                    raise TypeError
                if not len(user_input) == 1:
                    raise ValueError

                # Route input
                user_input = str(user_input)
                if user_input.lower() == "y":
                    return True
                elif user_input.lower() == "n":
                    return False
                else:
                    print("Please enter y or n.")
                    continue

            # Error handling
            except TypeError:
                print("Enter a character.")
                continue

            except ValueError:
                print("Enter one character.")
                continue

        return False

    def play(self) -> Player | None:
        """Contains the logic for the game loop. Returns the winner of the game or None if the user doesn't want to play again."""

        self.deal_cards()

        # self.take_first_turn(self.current_player)
        #
        # self.take_turn()

        for player in self.players:
            print(player)

        winner = self.players[0]  # PLACEHOLDER

        winner.prev_winner = True
        print(f"{winner.name} has won the game. Congratulations!")

        replay = self.query_for_replay()
        if replay:
            return winner

        return None

import random

from game import Game
from player import Player


def get_num_players() -> int:
    while True:
        try:
            num_players = int(input("How many players will play? "))
            if num_players < 2:
                print("Need at least 2 players.")
                continue
            elif num_players > 7:
                print("Cannot have more than 7 players")
                continue

            return num_players
        except TypeError:
            print("Enter a number")
            continue


def make_players(num_players: int) -> list[Player]:
    print("Enter each player's name: ")
    players = []
    names = []
    for i in range(num_players):
        while True:
            name = str(input(f"Player {i + 1}'s name: "))
            if name != "" and name not in names:
                player = Player(name)
                players.append(player)
                names.append(name)
            elif name == "":
                print("Enter a name.")
                continue
            elif name in names:
                print("Enter a unique name.")
                continue

            break

    return players


def run_game_loop(players: list[Player], first_player: Player) -> None:
    g = Game(players, first_player)
    prev_winner = g.play()  # returns None if not playing again
    while prev_winner:
        g = Game(players, prev_winner)
        prev_winner = g.play()
        if prev_winner:
            continue
        break


def main() -> None:
    num_players = get_num_players()

    players = make_players(num_players)

    rand_idx = random.randrange(0, num_players)
    first_player = players[rand_idx]

    run_game_loop(players, first_player)

    print("Game ended.")


if __name__ == "__main__":
    main()

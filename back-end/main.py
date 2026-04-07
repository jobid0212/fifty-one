import random

from game import Game
from player import Player


def main() -> None:
    while True:
        try:
            num_players = int(input("How many players will play? "))
            if num_players < 2:
                print("Need at least 2 players.")
                continue
            elif num_players > 7:
                print("Cannot have more than 7 players")
                continue

            break
        except ValueError:
            print("Enter a number")
            continue

    print("Enter each player's name: ")
    players = []
    for i in range(num_players):
        name = str(input(f"Player {i + 1}'s name: "))
        players.append(Player(name))

    rand_idx = random.randrange(0, num_players)
    prev_winner = players[rand_idx]

    playing = True
    while playing:
        g = Game(players, prev_winner)
        prev_winner = g.play()  # returns None if not playing again
        if prev_winner:
            continue
        break

    print("Game successfully ended.")


if __name__ == "__main__":
    main()

# A "meld" is the term for the grouping of cards you place down (runs or sets)

from card import Card
from suits import Suits
from values import Values


class Meld:
    def __init__(self, cards: list[Card]):
        self.cards = cards
        self.order_cards()
        self.playable_cards = self.find_playable()
        self.is_run = self.determine_is_run()

    def __str__(self) -> str:
        s = ""
        for card in self.cards:
            s += str(card) + "\n"
        s += "\n"
        return s

    # HANDLE IF 2 JOKERS ARE BEING PLACED DOWN?
    def determine_is_run(self) -> bool:
        """Determines if the given cards are a run. Returns true if so, false if its a set."""
        nums = []
        for card in self.cards:
            num = card.value.value
            if num in nums:
                return False

            nums.append(num)

        return True

    def order_cards(self) -> None:
        self.cards = sorted(self.cards)

    def find_playable(self) -> list[Card]:
        playable_list = []
        if self.is_run:
            suit = self.cards[0].suit
            if self.cards[0].value != Values.ACE:
                left_value = self.cards[0].value.value - 1
                left_card = Card(suit, Values(left_value))
                playable_list.append(left_card)

            if self.cards[-1].value != Values.ACE:
                right_value = self.cards[-1].value.value + 1
                right_card = Card(suit, Values(right_value))
                playable_list.append(right_card)

        else:
            suit_list = list(Suits)
            suit_list.remove(Suits.JOKER)
            for card in self.cards:
                suit_list.remove(card.suit)

            suit = suit_list[0]
            value = self.cards[0].value

            card = Card(suit, value)
            playable_list.append(card)

        playable_list.append(Card(Suits.JOKER, Values.ACE))

        return playable_list

    def check_can_be_added(self, card: Card) -> bool:
        playables = self.find_playable()
        if card in playables:
            return True

        return False

    def add(self, card: Card) -> None:
        self.cards.append(card)
        self.order_cards()
        self.find_playable()

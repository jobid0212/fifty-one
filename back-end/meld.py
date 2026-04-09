# A "meld" is the term for the grouping of cards you place down (runs or sets)

from card import Card


class Meld:
    def __init__(self, cards: list[Card]):
        self.cards = cards
        self.playable_cards = []
        self.order_cards()

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
        # TODO: implement
        pass

    def check_can_be_added(self, card: Card) -> bool:
        playables = self.find_playable()
        if card in playables:
            return True

        return False

    def add(self, card: Card) -> None:
        self.cards.append(card)
        self.order_cards()

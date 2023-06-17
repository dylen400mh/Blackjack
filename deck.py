from card import Card
import random  # used to shuffle deck


class Deck:

    def __init__(self):
        self.cards = []

        # adds each card to cards array
        for suit in Card.suits:
            for rank in Card.ranks:

                card = Card(rank, suit)

                self.cards.append(card)

    # shuffles cards
    def shuffle(self):
        random.shuffle(self.cards)

    # deals/removes a card from deck
    def deal(self):
        return self.cards.pop()

from card import Card

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in Card.suits:
            for rank in Card.ranks:

                card = Card(rank, suit)

                self.all_cards.append(card)




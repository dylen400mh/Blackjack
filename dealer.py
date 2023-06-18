from card import Card

class Dealer():

    def __init__(self):
        self.hand = []
        self.hand_value = 0

    def __str__(self):
        return f"Dealer's Hand:\n\t{self.hand[0]}\n\tCARD HIDDEN"
    
    # determines how many points the user has in their hand
    def set_hand_value(self):
        for card in self.hand:
            self.hand_value += Card.values[card.rank]

    def get_hand_value(self):
        return self.hand_value


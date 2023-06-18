from card import Card

class Dealer():

    def __init__(self):
        self.hand = []
        self.hand_value = 0
    
    # determines how many points the user has in their hand
    def set_hand_value(self):
        hand_value = 0

        for card in self.hand:
            hand_value += Card.values[card.rank]

    def get_hand_value(self):
        return self.hand_value

    


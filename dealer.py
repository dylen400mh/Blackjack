from card import Card

class Dealer():

    def __init__(self):
        self.hand = []
        self.hand_value = 0
    
    # determines how many points the user has in their hand
    def update_hand_value(self):

        self.hand_value = 0 #reset this and count all cards

        for card in self.hand:
            self.hand_value += card.value
        
        return self.hand_value



    


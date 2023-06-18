from dealer import Dealer

# Player class inherits from Dealer class
class Player(Dealer):

    def __init__(self):
        Dealer.__init__(self)
        self.chips = 100 # player starts with 100 chips
    
    # places a bet
    def place_bet(self, chips):
        self.chips -= chips

    # claim winnings (must multiply by 2 to account for the amount we originally bet)
    def claim_winnings(self, chips):
        self.chips += chips * 2
from dealer import Dealer

# Player class inherits from Dealer class
class Player(Dealer):

    def __init__(self, chips = 100):
        Dealer.__init__(self)
        self.chips = chips # player starts with 100 chips, and keeps his number of chips on all consecutive games
        self.is_playing = True # player starts playing first
    
    # places a bet
    def place_bet(self, chips):
        self.chips -= chips

    # claim winnings
    def claim_winnings(self, chips):
        self.chips += chips 
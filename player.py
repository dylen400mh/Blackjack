class Player:

    def __init__(self):
        self.chips = 100 # player starts with 100 chips
    
    # places a bet
    def place_bet(self, chips):
        self.chips -= chips
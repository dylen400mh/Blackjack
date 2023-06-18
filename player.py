from dealer import Dealer

# Player class inherits from Dealer class
class Player(Dealer):

    def __init__(self):
        self.chips = 100 # player starts with 100 chips
    
    # places a bet
    def place_bet(self, chips):
        self.chips -= chips

    def __str__(self):
        print("Player's Hand:")
        print("\t" + self.hand[0])
        print("\t" + self.hand[1])
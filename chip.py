class Chip:

    chips_on_table = 0

    def __init__(self):
        self.chips = 100 # player starts with 100 chips
    
    # places a bet
    def place_bet(self, chips):
        self.chips -= chips
        chips_on_table += chips * 2 # player and dealer will each add the same number of chips to the table
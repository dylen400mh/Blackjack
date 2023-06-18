class Dealer():

    def __init__(self):
        self.hand = []

    def __str__(self):
        return f"Dealer's Hand:\n\t{self.hand[0]}\n\tCARD HIDDEN"
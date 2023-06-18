class Dealer():

    def __init__(self):
        self.hand = []

    def __str__(self):
        print("Dealer's Hand:")
        print("\t" + self.hand[0])
        print("\tCARD HIDDEN")
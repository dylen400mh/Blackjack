from card import Card
from deck import Deck
from player import Player


# run code here
if __name__ == "__main__":

    pass
    
    # First, create a deck of 52 cards

    deck = Deck()
    
    # Shuffle the deck

    deck.shuffle()

    # initialize player object

    player = Player()

    print("Welcome to Blackjack! The goal is to get as close to 21 as possible without going over!")
    print("The dealer will hit until they reach 17. Aces can count as 1 or 11.")

    # Ask the player for their bet
    
    print(f"You currently have {player.chips} chips.")

    while True:
        try:
          bet = int(input("Place your bet: "))
        except TypeError:
            print("Please enter a valid number.")
        else:
            if bet > player.chips:
                print("You have an insufficient number of chips. Please try again.")
            else:
                player.place_bet(bet)
                break
        


    # Make sure bet doesn't exceed their chips

    # deal two cards to player and dealer

    # show only one of dealers cards; other is hidden
    
    # show both of player's cards

    # ask the player to hit and take another card

    # if they don't bust (go over 21) ask again

    # if player stands, play dealer's hand. Dealer will always hit until their value is >= 17

    # determine winner and adjust chips accordingly

    # ask player to play again



from card import Card
from deck import Deck
from player import Player
from dealer import Dealer

# determines how many points the user has in their hand
def hand_value(user):
    hand_value = 0

    for card in user.hand:
        hand_value += Card.values[card.rank]
    
    return hand_value


# run code here
if __name__ == "__main__":

    pass

    # First, create a deck of 52 cards

    deck = Deck()

    # Shuffle the deck

    deck.shuffle()

    # initialize player and dealer objects

    player = Player()
    dealer = Dealer()

    print("Welcome to Blackjack! The goal is to get as close to 21 as possible without going over!")
    print("The dealer will hit until they reach 17. Aces can count as 1 or 11.\n")

    # Ask the player for their bet

    print(f"You currently have {player.chips} chips.")

    while True:
        try:
            bet = int(input("Place your bet: "))
        except:
            print("Please enter a valid number.")
        else:
            # Make sure bet doesn't exceed their chips
            if bet > player.chips:
                print("You have an insufficient number of chips. Please try again.")
            elif bet < 1:
                print("Your must bet at least 1 chip. Please try again.")
            else:
                player.place_bet(bet)
                break

    # deal two cards to player and dealer

    for _ in range(2):
        player.hand.append(deck.deal())
        dealer.hand.append(deck.deal())

    # show only one of dealers cards; other is hidden
    # show both of player's cards
    print(dealer)
    print(player)

    # determine hand value of the player

    

    player.set_hand_value()

    # ask the player to hit and take another card
    # if they don't bust (go over 21) ask again

    while player.hand_value

    # if player stands, play dealer's hand. Dealer will always hit until their value is >= 17

    # determine winner and adjust chips accordingly

    # ask player to play again

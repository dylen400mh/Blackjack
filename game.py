from card import Card
from deck import Deck
from player import Player
from dealer import Dealer

# method to print player and dealer hands
def print_hands():

    print("Dealer's Hand:")
    
    if player_hitting:
        print(dealer.hand[0])
        print("CARD HIDDEN")
    else:
        for card in dealer.hand:
            print(card)

    print("Player's Hand:")
    for card in player.hand:
        print(card)

def update_hand_values():
    player.set_hand_value()
    dealer.set_hand_value()
    
    return player.get_hand_value(), dealer.get_hand_value()


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


    # determine hand value of the player and dealer

    player_hand_value, dealer_hand_value = update_hand_values()

    # we will use this boolean to determine whether the dealer's card should be hidden or shown
    player_hitting = True

    # ask the player to hit and take another card
    # if they don't bust (go over 21) ask again
    while player_hand_value < 21 and player_hitting:
        ans = ""

        # show only one of dealers cards; other is hidden
        # show both of player's cards
        print_hands()

        while ans.upper() not in ["H", "S"]:
            ans = input("Would you like to hit or stand? ('H' or 'S'): ")

            if ans.upper() not in ["H", "S"]:
                print("Invalid Input. Please try again.")
        
        # if player hits, deal them a card and update their hand value
        if ans.upper() == "H":
            player.hand.append(deck.deal())

            player_hand_value = update_hand_values()[0] # we are only concerned in modifying the player's hand value right now

        # break out if they choose to stand
        if ans.upper() == "S":
            player_hitting = False
    
    # if player gets a blackjack (21 points), claim winnings (doubled to account for original bet)
    if player_hand_value == 21:
        print("BLACKJACK!")
        player.claim_winnings(bet * 2)
        
    # if player busts (goes over 21)
    if player_hand_value > 21:
        print("Player busts!")
    


    # if player stands, play dealer's hand. Dealer will always hit until their value is >= 17

    # determine winner and adjust chips accordingly

    # ask player to play again


'''
TODOS

2. if player stands, play dealer's hand until >= 17. What if they bust?
3. Determine winner and adjust chips
4. make a loop to play again until they quit
5. adjust spacing/tabs to make interface look nicer
6. are there any ways to clean up my code?
7. consider adding comments to help myself and others understand the code
'''
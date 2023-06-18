# Python Blackjack Card Game
This is a command-line implementation of the classic casino game Blackjack, also known as 21, developed using Python.

## Game Rules
Blackjack is a card game played against a dealer. The objective of the game is to get a hand value as close to 21 as possible without exceeding it. Here are the basic rules:

1. Each player is dealt two cards initially, while the dealer receives one card facing up and one facing down.

2. Numbered cards (2-10) are worth their face value, face cards (Jack, Queen, King) are worth 10, and an Ace can be worth either 1 or 11.

3. The player can request additional cards ("Hit") to increase their hand value or choose to stop ("Stand") to keep their current hand.

4. If the player's hand value exceeds 21, they "Bust" and lose the game.

5. Once the player decides to stand, the dealer reveals their facedown card.

6. The dealer must hit until their hand value is 17 or higher.

7. If the dealer's hand exceeds 21, they bust, and the player wins.

8. If neither the player nor the dealer busts, the hand with a value closest to 21 wins the game.

## Features
- The game supports a single player playing against the computerized dealer.

- The player can choose to hit or stand based on the current hand value.

- The game displays the player's and dealer's hands, as well as their current hand values.

- At the end of each round, the game announces the winner.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Setup

1. Clone the repository or download the source code as a ZIP file.

2. Open a terminal or command prompt and navigate to the project directory.
### Running the Game

1. Run the following command to start the Blackjack game:

``python blackjack.py``

2. Follow the prompts and make your decisions by typing the corresponding options.

3. The game will display the cards, current hand values, and announce the winner at the end of each round.

4. To play again, simply follow the prompts.

## Project Structure

The project contains the following files:

- game.py: The main Python script that implements the game logic.
  
- card.py: A module that defines the Card class to represent a playing card.
  
- deck.py: A module that defines the Deck class to represent a deck of cards and provides functions for shuffling and dealing.
  
- dealer.py: A module that defines the Dealer class to represent a dealer in the game
  
- player.py: A module inheriting the Dealer class that defines the Player class to represent a player in the game, having additional functionality such as placing a bet and claiming winnings.

- README.md: This README file providing information about the project.

## Acknowledgments

This game was developed as a learning project to practice Python Object Oriented Programming and demonstrate command-line interaction.

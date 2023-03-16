# Blackjack-Game

This is a simple text-based Blackjack game implemented in Python. It includes a basic user interface and provides a fun way to practice your Blackjack skills without any monetary risk.

## Requirements

- Python 3

## How to run the game

To run the game, simply execute the `main.py` file:

```bash
python main.py
```

## Game rules

The game is played with a standard deck of 52 playing cards. The goal is to have a hand value as close to 21 as possible without going over. Face cards (K, Q, J) are worth 10 points, Aces can be worth 11 or 1, and numbered cards are worth their face value.

The game starts by dealing two cards to both the player and the dealer. The dealer shows one card face up, while the other card remains hidden. The player can see both of their cards and their total value.

### The player has two options:

- __Hit (h)__: Draw another card to try to improve the hand value.
- __Stand (s)__: Keep the current hand and end the turn.

If the player's hand value exceeds 21, the player busts, and the dealer wins. If the player stands, the dealer reveals their hidden card and draws more cards if their hand value is less than 17. If the dealer's hand value exceeds 21, the dealer busts, and the player wins. If both the player and the dealer stand, the hand with the value closest to 21 wins.

To exit the game, simply choose not to play again when prompted.

### Implementation details

The game is implemented using three main classes:

-__`Card`__: Represents a playing card with a suit and rank.

-__`Deck`__: Represents a deck of 52 playing cards and provides methods to shuffle and draw cards.

-__`Hand`__: Represents a hand of cards, calculates the hand value, and provides a string representation of the hand.



The __`blackjack_game`__ function controls the game flow, and the print_hands function displays the current hands of the player and the dealer. The main loop at the bottom of the script allows for replaying the game.

Enjoy the game and good luck!

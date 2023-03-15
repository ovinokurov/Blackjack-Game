import random

class Card:
    suits = ['♠', '♣', '♥', '♦']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def value(self):
        if self.rank == 'A':
            return 11
        elif self.rank in ['K', 'Q', 'J']:
            return 10
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in Card.suits for r in Card.ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)

def print_hands(player_hand, dealer_hand, hide_dealer_card=True):
    if hide_dealer_card:
        print(f"Dealer: {dealer_hand.cards[0]} ??")
    else:
        print(f"Dealer: {dealer_hand} ({dealer_hand.value()})")
    print(f"Player: {player_hand} ({player_hand.value()})")

def blackjack_game():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    for _ in range(2):
        player_hand.add_card(deck.draw_card())
        dealer_hand.add_card(deck.draw_card())

    print_hands(player_hand, dealer_hand)

    while True:
        action = input("Enter 'h' for hit, 's' for stand: ").lower()
        if action == 'h':
            player_hand.add_card(deck.draw_card())
            print_hands(player_hand, dealer_hand)
            if player_hand.value() > 21:
                print("Player busts! Dealer wins.")
                return
        elif action == 's':
            break

    print_hands(player_hand, dealer_hand, hide_dealer_card=False)

    while dealer_hand.value() < 17:
        dealer_hand.add_card(deck.draw_card())
        print_hands(player_hand, dealer_hand, hide_dealer_card=False)

    if dealer_hand.value() > 21:
        print("Dealer busts! Player wins.")
    elif dealer_hand.value() < player_hand.value():
        print("Player wins!")
    elif dealer_hand.value() > player_hand.value():
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    while True:
        blackjack_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

import random
import collections

SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
VALUES = ['AS', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def create_deck():
    deck = []

    for suit in SUITS:
        for value in VALUES:
            deck.append((suit, value))

    return deck

def pick_cards(deck, number_of_cards):
    pick = random.sample(deck, number_of_cards)

    return pick


def main(number_of_cards, number_of_simulations):
    deck = create_deck()
    
    hands = []
    for _ in range(number_of_simulations):
        hand = pick_cards(deck,number_of_cards)
        hands.append(hand)
    
    pairs = 0
    for hand in hands:
        
        VALUES = []
        for carta in hand:
            VALUES.append(carta[1])

        counter = dict(collections.Counter(VALUES))
        for val in counter.values():
            if val == 2:
                pairs += 1
                break

    pairs_probabilities = pairs / number_of_simulations
    print(f"The probability to obtain pairs picking {number_of_cards} cards in the deck is {pairs_probabilities}")

if __name__ == '__main__':
    number_of_cards = int(input("How many cards do you want to pick? "))
    number_of_simulations = int(input("How many simulations do you want to run? "))

    main(number_of_cards, number_of_simulations)
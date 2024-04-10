# Author: Corbin Lienau

import random


# Define a class representing a deck of playing cards
class CardDeck:
    def __init__(self):
        # Initialize the deck with standard playing card values and suits
        self.cards = ['Ace', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        # Create the deck by combining cards and suits, then shuffle it
        self.deck = [(card, suit)
                     for card in self.cards for suit in self.suits]
        random.shuffle(self.deck)
        # Initialize variables to track drawn cards and various counts
        self.drawn_cards = []
        self.total_draws = len(self.drawn_cards)
        self.total_cards = len(self.deck)
        self.red_card_count = 26
        self.black_card_count = 26
        self.spade_card_count = 13
        self.club_card_count = 13
        self.heart_card_count = 13
        self.diamond_card_count = 13

    # Method to draw a card from the deck
    def draw_card(self):
        if self.deck:
            card = self.deck.pop()
            self.drawn_cards.append(card)
            return card
        else:
            return None

    # Method to update counts based on the drawn card
    def update_deck(self, card):
        self.total_cards -= 1
        suit = card[1]
        if suit == 'Hearts':
            self.heart_card_count -= 1
        elif suit == 'Diamonds':
            self.diamond_card_count -= 1
        elif suit == 'Clubs':
            self.club_card_count -= 1
        elif suit == 'Spades':
            self.spade_card_count -= 1
        if card[1] in ['Hearts', 'Diamonds']:
            self.red_card_count -= 1
        else:
            self.black_card_count -= 1

    # Method to calculate the probability of drawing a specific card
    def calculate_unique_probability(self, target_card):
        cards_remaining = self.total_cards - self.total_draws
        if cards_remaining < 1:
            return "No cards left in the deck."
        unique_probability = 1 / cards_remaining
        return f"Unique Probability of drawing {target_card} after " \
               f"{len(self.drawn_cards)} draws: {unique_probability * 100:.2f}%"

    # Method to calculate the dependent probability of drawing a specific card
    def calculate_dependent_probability(self, target_card):
        cards_remaining = self.total_cards - self.total_draws
        dependent_probability = 1
        for i in range(len(self.drawn_cards)):
            remaining_cards = cards_remaining - i
            if remaining_cards == 0:
                dependent_probability = 0
                break
            dependent_probability *= 1 / remaining_cards
        return f"After {len(self.drawn_cards)} draw, the dependent probability of drawing the card " \
               f"{target_card}, considering all possible unique orderings, " \
               f"is approximately: {dependent_probability * 100:.10f}%"

    # Method to calculate the probability of drawing a card of the same color as the target card
    def calculate_color_probability(self, target_card):
        if target_card[1] in ['Hearts', 'Diamonds']:
            numerator = self.red_card_count
        else:
            numerator = self.black_card_count

        cards_remaining = self.total_cards - self.total_draws
        color_probability = numerator / cards_remaining

        card_color = "red" if target_card[1] in [
            'Hearts', 'Diamonds'] else "black"

        return f"Probability of draw #" \
               f"{len(self.drawn_cards)} being {card_color} : {color_probability * 100:.2f}%"

    # Method to calculate the probability of drawing a card of the same suit as the target card
    def calculate_suit_probability(self, target_card):
        suit = target_card[1]

        if suit == 'Hearts':
            print_suit = "Hearts"
            numerator = self.heart_card_count
        elif suit == 'Diamonds':
            print_suit = "Diamonds"
            numerator = self.diamond_card_count
        elif suit == 'Clubs':
            print_suit = "Clubs"
            numerator = self.club_card_count
        else:
            print_suit = "Spades"
            numerator = self.spade_card_count

        card_remaining = self.total_cards - self.total_draws
        suit_probability = numerator / card_remaining

        return f"Probability of draw #" \
               f"{len(self.drawn_cards)} being {print_suit.lower()} : {suit_probability * 100:.2f}%"


# Main function to run the program
def main():
    try:
        # Create a deck object
        deck = CardDeck()
        # Prompt the user for the number of draws
        num_draws = int(input("Enter the number of times to draw a card: "))
        if num_draws <= 0:
            print("Please enter a positive integer greater than 0.")
            return
        if num_draws > 52:
            print("You can only draw up to 52 cards from the deck.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Loop to draw cards and calculate probabilities
    for _ in range(num_draws):
        drawn_card = deck.draw_card()

        unique_probability = deck.calculate_unique_probability(drawn_card)
        print(unique_probability)

        dependent_probability = deck.calculate_dependent_probability(
            drawn_card)
        print(dependent_probability)

        color_probability = deck.calculate_color_probability(drawn_card)
        print(color_probability)

        suit_probability = deck.calculate_suit_probability(drawn_card)
        print(suit_probability)
        print()

        deck.update_deck(drawn_card)


# Entry point of the program
if __name__ == "__main__":
    main()

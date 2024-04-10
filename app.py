from flask import Flask, render_template, request
import random
# Assuming you have your CardDeck class in card_deck.py
from card_deck import CardDeck

app = Flask(__name__)

# Your CardDeck instance
deck = CardDeck()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/draw', methods=['POST'])
def draw():
    num_draws = int(request.form['num_draws'])

    if num_draws <= 0:
        return "Please enter a positive integer greater than 0."
    if num_draws > 52:
        return "You can only draw up to 52 cards from the deck."

    drawn_cards_info = []

    for _ in range(num_draws):
        drawn_card = deck.draw_card()

        if drawn_card is not None:
            # Convert the drawn card tuple to string format
            card_name = f"{drawn_card[0]} of {drawn_card[1]}"
            # Calculate probabilities
            unique_probability = deck.calculate_unique_probability(card_name)
            dependent_probability = deck.calculate_dependent_probability(
                card_name)
            color_probability = deck.calculate_color_probability(card_name)
            suit_probability = deck.calculate_suit_probability(card_name)

            drawn_cards_info.append({
                'drawn_card': card_name,
                'unique_probability': unique_probability,
                'dependent_probability': dependent_probability,
                'color_probability': color_probability,
                'suit_probability': suit_probability
            })

            deck.update_deck(drawn_card)
        else:
            print("Error: No card was drawn.")

    return render_template('draw.html', drawn_cards_info=drawn_cards_info)


if __name__ == '__main__':
    app.run(debug=True)

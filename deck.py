from card import Card
import random

class Deck:
    def __init__(self):
        cards = []

        for suit in ['h', 's', 'd', 'c']:
            for number in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                cards.append(Card(suit, number))

        self.cards = cards

    def shuffleCards(self):
        random.shuffle(self.cards)

    def showDeck(self):
        for card in self.cards:
            print(card.showCard())

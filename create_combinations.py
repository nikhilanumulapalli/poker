from deck import Deck
# import pandas as pd
import time
import csv
from card import Card
from hand import Hand

newDeck = Deck()

with open('combinations.csv', 'w') as file:
    output = csv.writer(file, delimiter=',')
    for i in range(len(newDeck.cards) - 6):
        start = time.time()
        for j in range(i+1, len(newDeck.cards) - 5):
            for k in range(j+1, len(newDeck.cards) - 4):
                possibleCombinations = []
                for l in range(k+1, len(newDeck.cards) - 3):
                    for m in range(l+1, len(newDeck.cards) - 2):
                        for n in range(m+1, len(newDeck.cards) - 1):
                            for o in range(n+1, len(newDeck.cards)):
                                new_row = [
                                    newDeck.cards[51 - i].showCard(),
                                    newDeck.cards[51 - j].showCard(),
                                    newDeck.cards[51 - k].showCard(),
                                    newDeck.cards[51 - l].showCard(),
                                    newDeck.cards[51 - m].showCard(),
                                    newDeck.cards[51 - n].showCard(),
                                    newDeck.cards[51 - o].showCard()
                                ]
                                new_hand = Hand([Card(s[0], s[1]) for s in new_row])
                                new_row.append(new_hand.category)
                                new_row.append(new_hand.bestCards)
                                possibleCombinations.append(new_row)
                output.writerows(possibleCombinations)
        print(time.time() - start, 51-6-i)

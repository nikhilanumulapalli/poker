from deck import Deck
# import pandas as pd
import time
import csv

newDeck = Deck()

# newDeck.showDeck()

with open('combinations.csv', 'a') as file:
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
                                possibleCombinations.append([
                                    newDeck.cards[51 - i].showCard(),
                                    newDeck.cards[51 - j].showCard(),
                                    newDeck.cards[51 - k].showCard(),
                                    newDeck.cards[51 - l].showCard(),
                                    newDeck.cards[51 - m].showCard(),
                                    newDeck.cards[51 - n].showCard(),
                                    newDeck.cards[51 - o].showCard()
                                ])
                output.writerows(possibleCombinations)
        print(time.time() - start, 51-6-i)
        # break

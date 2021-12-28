class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        if number == 'A':
            self.value = 14
        elif number == 'K':
            self.value = 13
        elif number == 'Q':
            self.value = 12
        elif number == 'J':
            self.value = 11
        else:
            self.value = int(number)
        self.hexValue = chr(96+self.value)

    # def getValue(self, card):
    #     return card.value

    def showCard(self):
        return self.suit+self.number

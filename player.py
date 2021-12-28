from card import Card
class Player:
    def __init__(self, name = "__"):
        self.playerName = name
        self.playerCards = []
        self.categoryRank = 0
        self.internalRank = 0
        self.category = ""
        self.hand = None

    def showPlayer(self):
        print("{}:".format(self.playerName))
        for card in self.playerCards:
            print(card.showCard(), end = " ")
        print()
        print("category: {}, category: {}, internalRank: {}, bestCards: {}"
        .format(self.category, self.category, self.internalRank, self.hand.bestCards))
        print()

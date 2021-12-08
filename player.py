from card import Card
class Player:
    def __init__(self, name = "__"):
        self.playerName = name
        self.playerCards = []
        self.categoryRank = 0
        self.internalRank = 0
        self.category = ""
        self.hand = ""

    def showPlayer(self):
        print("{}:".format(self.playerName))
        for card in self.playerCards:
            print(card.showCard(), end = " ")
        print()
        print("category: {}, categoryRank: {}, internalRank: {}".format(
        self.category, self.categoryRank, self.internalRank))

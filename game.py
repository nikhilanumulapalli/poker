from deck import Deck
from player import Player
from hand import Hand

class Game:
    def __init__(self, numberOfPlayers):
        self.currentDeck = Deck()
        self.currentDeck.shuffleCards()
        self.numberOfPlayers = numberOfPlayers
        self.players = [Player() for _ in range(numberOfPlayers)]
        self.playersCards = []
        self.flop = []
        self.bestPlayers = []
        # self.turn = ''
        # self.river = ''

    def deal(self):
        playersCards = []
        for player in range(self.numberOfPlayers):
            playersCards.append([self.currentDeck.cards.pop()])

        for player in range(self.numberOfPlayers):
            playersCards[player].append(self.currentDeck.cards.pop())

        self.playersCards = playersCards
        for i, playerCards in enumerate(playersCards):
            self.players[i].playerCards = playerCards

        #flop
        self.currentDeck.cards.pop()
        self.flop.append(self.currentDeck.cards.pop())
        self.flop.append(self.currentDeck.cards.pop())
        self.flop.append(self.currentDeck.cards.pop())

        #trun
        self.currentDeck.cards.pop()
        # self.turn = self.currentDeck.cards.pop()
        self.flop.append(self.currentDeck.cards.pop())

        #river
        self.currentDeck.cards.pop()
        # self.river = self.currentDeck.cards.pop()
        self.flop.append(self.currentDeck.cards.pop())


    def showPlayerCards(self):
        numberOfPlayers = self.numberOfPlayers

        for i in range(numberOfPlayers):
            print('player{}: {} {} {}, {}'.format(i,
            self.playersCards[i][0].showCard(), self.playersCards[i][1].showCard(), self.players[i].hand.category, self.players[i].hand.bestCards))

    # def openCards(self):
    #     for i in [1,2,3,5,7]:
    #         print(self.currentDeck.cards[i].showCard())

    def showTable(self):
        for card in self.flop:
            print(card.showCard(), end = " ")
        print()

    def calculateTheWinner(self):
        bestRank = 10
        # print("__________", len(self.players))
        for player in self.players:
            # print(player.playerCards)
            playerHand = self.flop.copy()
            playerHand.extend(player.playerCards)
            hand = Hand(playerHand)
            player.hand = hand
            hand.pickCategory()

            player.category = hand.category
            player.categoryRank = hand.rank
            # print(player.categoryRank, "__________________")

            if hand.rank == bestRank:
                # print(hand.rank, "____", len(self.bestPlayers))
                self.bestPlayers.append(player)
            elif hand.rank < bestRank:
                bestRank = hand.rank
                self.bestPlayers = [player]
                # print(len(self.bestPlayers), hand.rank, "____")

        for player in self.bestPlayers:
            player.showPlayer()

        # danger code starts, don't uncomment it
        # ranks = {}
        # for player in self.players:
        #     playerHand = self.flop.copy()
        #     playerHand.extend(player.playerCards)
        #     player.hand = Hand(playerHand)
        #     hand.pickCategory()
        #
        #     player.category = hand.category
        #     player.categoryRank = hand.rank
        #
        #     if player.categoryRank in ranks:
        #         ranks[player.categoryRank].append((player, hand))
        #     else:
        #         ranks[player.categoryRank] = [(player, hand)]
        # danger code ends, don't uncomment it

        # for rank in ranks:
        #     if len(ranks[rank]) > 1:
        #         self.calculateInternalRank(rank, ranks[rank])



    # def calculateInternalRank(self, rank, players):
    #     if rank == 10:

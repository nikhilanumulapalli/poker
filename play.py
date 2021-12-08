from game import Game

newGame = Game(4)

newGame.deal()

newGame.showTable()
newGame.showPlayerCards()

newGame.calculateTheWinner()

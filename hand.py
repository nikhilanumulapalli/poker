from card import Card

class Hand:
    def __init__(self, hand):
        self.hand = hand #[Card()]
        self.category = self.pickCategory()
        self.rank = 0

    def isStraight(self, numbers):
        if 14 in numbers:
            numbers.append(1)
        numbers.sort()

        newNums = []
        for i in range(len(numbers) - 1):
            newNums.append(numbers[i] - numbers[i+1])

        # print(numbers, newNums)

        for i in range(len(newNums)-3):
            if newNums[i:i+4].count(-1) == -4:
                return True

        return False

    def getValue(self, card):
        return card.value

    def sortHand(self):
        # if self.rank == 10:
        self.hand.sort(key=self.getValue, reverse=True)

    def pickCategory(self):
        # print()
        # for card in self.hand:
        #     print(card.showCard(), end = " ")

        suitFrequency = {"h": 0, "s": 0, "c": 0, "d": 0}

        for card in self.hand:
            suitFrequency[card.suit] += 1

        for suit in suitFrequency:
            if suitFrequency[suit] >= 5:
                flushCardValues = [card.value for card in self.hand if card.suit == suit]

                for num in range(10, 15):
                    if num not in flushCardValues:
                        break
                else:
                    self.rank = 1
                    return "Royal Flush"

                if self.isStraight(flushCardValues):
                    self.rank = 2
                    return "Straight Flush"

                else:
                    self.rank = 5
                    return "Flush"

            else:
                cardValues = [card.value for card in self.hand]

                frequency = {}
                for value in cardValues:
                    if value in frequency:
                        frequency[value] += 1
                    else:
                        frequency[value] = 1

                for _, value in frequency.items():
                    if value == 4:
                        self.rank = 3
                        return "Four of a kind"

                frequencyCount = {3: 0, 2: 0}
                for _, value in frequency.items():
                    if value in (3,2):
                        frequencyCount[value] += 1

                category = "High Card"
                self.rank = 10
                if frequencyCount[3] > 1 or (frequencyCount[3] == 1 and frequencyCount[2] >= 1):
                    self.rank = 4
                    return "Full House"
                elif frequencyCount[3] == 1:
                    self.rank = 7
                    category = "Three of a kind"
                elif frequencyCount[2] >= 2:
                    self.rank = 8
                    category = "Two pair"
                elif frequencyCount[2] == 1:
                    self.rank = 9
                    category = "Pair"

                if self.isStraight(cardValues):
                    self.rank = 6
                    return "Straight"

                # self.findRank(cardValues, category)
                return category

                # foundThree = False
                # for key, value in frequency.items():
                #     if value == 3:
                #         frequency.pop(key)
                #         foundThree = True
                #         break
                #
                # category = "High Card"
                # if foundThree:
                #     for key, value in frequency.items():
                #         if value >= 2:
                #             return "Full House"
                #     category = "Three of a kind"
                #
                # else:
                #     foundTow = False
                #     for key, value in frequency.items():
                #         if value == 2:
                #             category = "Three of a kind"


    # def findRank(self, numbers, category):
    #     topNums = sorted(numbers)[:5]
    #     # print(topNums)
    #     if category == "High Card":
    #         self.score = sum(topNums)





# def check(hand):
#     print(hand.pickCategory(), hand.rank)
#
#
#
#
# check(Hand([Card("h", "A"), Card("h", "10"), Card("h", "Q"),
# Card("h", "J"), Card("h", "K"), Card("h", "9"), Card("h", "8")]))
#
# check(Hand([Card("h", "A"), Card("h", "K"), Card("h", "Q"),
# Card("h", "6"), Card("h", "10"), Card("h", "9"), Card("h", "8")]))
#
# check(Hand([Card("h", "A"), Card("h", "3"), Card("h", "5"),
# Card("h", "J"), Card("h", "4"), Card("h", "9"), Card("h", "2")]))
#
# check(Hand([Card("h", "4"), Card("h", "K"), Card("h", "Q"),
# Card("h", "J"), Card("h", "10"), Card("h", "9"), Card("s", "8")]))
#
# check(Hand([Card("h", "4"), Card("c", "K"), Card("h", "Q"),
# Card("h", "J"), Card("h", "10"), Card("h", "9"), Card("s", "8")]))
#
# check(Hand([Card("h", "4"), Card("c", "K"), Card("c", "Q"),
# Card("h", "J"), Card("h", "10"), Card("h", "9"), Card("s", "8")]))
#
# check(Hand([Card("s", "4"), Card("c", "4"), Card("c", "Q"),
# Card("h", "J"), Card("h", "4"), Card("h", "9"), Card("s", "9")]))
#
# check(Hand([Card("s", "4"), Card("c", "4"), Card("c", "9"),
# Card("h", "J"), Card("h", "4"), Card("h", "9"), Card("s", "9")]))
#
# check(Hand([Card("s", "4"), Card("c", "4"), Card("c", "Q"),
# Card("h", "J"), Card("h", "4"), Card("h", "K"), Card("s", "9")]))
#
# check(Hand([Card("s", "4"), Card("c", "4"), Card("c", "Q"),
# Card("h", "J"), Card("h", "K"), Card("h", "9"), Card("s", "9")]))
#
# check(Hand([Card("s", "4"), Card("c", "4"), Card("c", "Q"),
# Card("h", "J"), Card("h", "3"), Card("h", "2"), Card("s", "9")]))
#
# check(Hand([Card("s", "4"), Card("c", "K"), Card("c", "Q"),
# Card("h", "J"), Card("h", "3"), Card("h", "2"), Card("s", "9")]))

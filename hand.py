from card import Card

class Hand:
    def __init__(self, hand):
        self.hand = hand #[Card()]
        self.rank = 0
        self.bestCards = "" #rank, bestCards will be updated in the next step
        self.category = self.pickCategory()

    def isStraight(self, numbers):
        isHandStraight = False
        if 14 in numbers:
            numbers.append(1)
        numbers.sort()

        newNums = []
        for i in range(len(numbers) - 1):
            newNums.append(numbers[i] - numbers[i+1])

        for i in range(len(newNums)-3):
            if newNums[i:i+4].count(-1) == -4:
                isHandStraight = True
                break
        if isHandStraight:
            bestCards = []
            for num in numbers[i:i+5]:
                bestCards.append(chr(96+num))
            self.bestCards = "".join(bestCards[::-1])

        return isHandStraight

    def getValue(self, card):
        return card.value

    def pickBestCards(self, frequency = {}, frequencyCount = {}):
        if self.rank == 10: #High card
            self.hand.sort(key=self.getValue, reverse=True)
            self.hand.pop(-1)
            self.hand.pop(-1)
            bestCards = [i.hexValue for i in self.hand]

        if self.rank == 3: #Four of a kind
            for key, value in frequency.items():
                if value == 4:
                    bestCards = [chr(96+key) for _ in range(4)]
                    break
            del frequency[key]

            bestCards.append(chr(96+max(frequency.keys())))

        if self.rank == 4: #Full House
            if frequencyCount[3] == 1 and frequencyCount[2] == 1:
                for key, value in frequency.items():
                    if value == 3:
                        bestCards = [chr(96+key) for _ in range(3)]

                for key, value in frequency.items():
                    if value == 2:
                        bestCards.append(chr(96+key))
                        bestCards.append(chr(96+key))

            if frequencyCount[3] > 1:
                triplets = []
                for key, value in frequency.items():
                    if value == 3:
                        triplets.append(key)
                triplets.sort(reverse = True)
                bestCards = [chr(96+triplets[i//3]) for i in range(5)]

            if frequencyCount[3] == 1 and frequencyCount[2] > 1:
                for key, value in frequency.items():
                    if value == 3:
                        bestCards = [chr(96+key) for _ in range(3)]

                biggestTwin = 0
                for key, value in frequency.items():
                    if value == 2:
                        biggestTwin = max(biggestTwin, key)

                bestCards.append(chr(96+biggestTwin))
                bestCards.append(chr(96+biggestTwin))

        if self.rank == 7: #Three of a kind
            for key, value in frequency.items():
                if value == 3:
                    bestCards = [chr(96+key) for _ in range(3)]
                    break
            del frequency[key]

            keys = list(frequency.keys())
            keys.sort(reverse = True)
            for key in keys[:2]:
                bestCards.append(chr(96+key))

        if self.rank == 8: #Two pair
            twins = []
            for key, value in frequency.items():
                if value == 2:
                    twins.append(key)

            for key in twins:
                del frequency[key]

            twins.sort(reverse = True)
            if len(twins) > 2:
                bestCards = [chr(96+twins[i//2]) for i in range(5)]
            elif len(twins) == 2:
                bestCards = [chr(96+twins[i//2]) for i in range(4)]
                bestCards.append(chr(96+max(frequency.keys())))

        if self.rank == 9: #Pair
            for key, value in frequency.items():
                if value == 2:
                    bestCards = [chr(96+key) for _ in range(2)]
                    break
            del frequency[key]

            keys = list(frequency.keys())
            keys.sort(reverse = True)
            # print(keys)
            for key in keys[:3]:
                bestCards.append(chr(96+key))

        self.bestCards = "".join(bestCards)

    def pickCategory(self):
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
                    self.bestCards = 'nmlkj'
                    return "Royal Flush"

                if self.isStraight(flushCardValues):
                    self.rank = 2
                    return "Straight Flush"

                else:
                    self.rank = 5
                    flushCardValues.sort(reverse=True)
                    self.bestCards = "".join(map(lambda x: chr(96+x), flushCardValues[:5]))
                    return "Flush"

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
                self.pickBestCards(frequency)
                return "Four of a kind"

        frequencyCount = {3: 0, 2: 0}
        for _, value in frequency.items():
            if value in (3,2):
                frequencyCount[value] += 1

        category = "High Card"
        self.rank = 10
        if frequencyCount[3] > 1 or (frequencyCount[3] == 1 and frequencyCount[2] >= 1):
            self.rank = 4
            self.pickBestCards(frequency, frequencyCount)
            return "Full House"
        elif frequencyCount[3] == 1:
            self.rank = 7
            self.pickBestCards(frequency)
            category = "Three of a kind"
        elif frequencyCount[2] >= 2:
            self.rank = 8
            self.pickBestCards(frequency)
            category = "Two pair"
        elif frequencyCount[2] == 1:
            self.rank = 9
            self.pickBestCards(frequency)
            category = "Pair"

        if self.isStraight(cardValues):
            self.rank = 6
            return "Straight"

        if self.rank == 10:
            self.pickBestCards()
        return category


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

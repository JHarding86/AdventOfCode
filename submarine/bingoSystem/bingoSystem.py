from submarine.bingoSystem.bingoCard import bingoCard

class bingoSystem:
    def __init__(self):
        self.callouts       = []
        self.cards          = []
        self.winningCallout = 0

        self.__readBingoInput()

        print("Bingo System Initialized")

        winningCard = self.playBingoFindingFirstWinner()
        winningCard.print()
        score = winningCard.calculateScore(self.winningCallout)
        print("Winning Card Score:", score)

        self.cards = []
        self.__readBingoInput()
        lastWinningCard = self.playBingoFindingLastWinner()
        lastWinningCard.print()
        score = lastWinningCard.calculateScore(self.winningCallout)
        print("Last Winning Card Score:", score)

    def __readBingoInput(self):
        with open('inputFiles/day4_input.txt') as f:

            self.callouts = list(map(int, f.readline().split(",")))

            #read blank line
            line = f.readline()

            while line != "":#this indicates the end of the file
                self.cards.append(self.__readCard(f))
                line = f.readline()
        f.close()

        for card in self.cards:
            card.print()

    def __readCard(self, file):
        rows = []
        for i in range(5):
            rows.append(file.readline())

        card = bingoCard(rows)

        return card

    def playBingoFindingFirstWinner(self):
        for callout in self.callouts:
            for card in self.cards:
                card.markNumber(callout)
                # card.print()
                if card.checkForBingo():
                    self.winningCallout = callout
                    return card

    def playBingoFindingLastWinner(self):
        for callout in self.callouts:
            i = 0
            while i < len(self.cards):
            # for i in range(len(self.cards)):
                self.cards[i].markNumber(callout)
                # card.print()
                if self.cards[i].checkForBingo():
                    if len(self.cards) == 1:
                        self.winningCallout = callout
                        return self.cards[i]
                    else:
                        self.cards.remove(self.cards[i])
                else:
                    i += 1
                    

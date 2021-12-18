from submarine.bingoSystem.bingoCard import bingoCard

class bingoSystem:
    def __init__(self):
        self.callouts       = []
        self.cards          = []
        self.winningCallout = 0

        self.__readBingoInput()

        print("Bingo System Initialized")

        winningCard = self.playBingo()
        winningCard.print()
        score = winningCard.calculateScore(self.winningCallout)
        print("Winning Card Score:", score)

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

    def playBingo(self):
        for callout in self.callouts:
            for card in self.cards:
                card.markNumber(callout)
                # card.print()
                if card.checkForBingo():
                    self.winningCallout = callout
                    return card

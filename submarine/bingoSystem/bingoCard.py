from submarine.bingoSystem.bingoCell import bingoCell

class bingoCard:
    def __init__(self, rawCard):

        self.card = []

        for rawRow in rawCard:
            rawRow = rawRow.replace("  ", " ")
            if rawRow[0] == " ":
                rawRow = rawRow[1:]
            cells = rawRow.split(" ")
            row = []
            for value in cells:
                row.append(bingoCell(value))
            self.card.append(row)
                
        print("Bingo Card Initialized")

    def markNumber(self, number):
        for row in self.card:
            for cell in row:
                if cell.value == number:
                    cell.marked = True
    
    def checkForBingo(self):
        #check for horizontal bingos
        for row in self.card:
            count = 0
            for cell in row:
                if cell.marked == True:
                    count += 1
            if count == 5:
                return True
        
        #check for vertical bingos
        for col in range(len(self.card[0])):
            count = 0
            for row in range(len(self.card)):
                if self.card[row][col].marked == True:
                    count += 1
            if count == 5:
                return True
        
    def calculateScore(self, winningCallout):
        total = 0
        for row in self.card:
            for cell in row:
                if cell.marked == False:
                    total += cell.value
        
        return total * winningCallout

    def print(self):
        for row in self.card:
            string = ""
            for cell in row:
                if cell.marked:
                    marked = "(X)"
                else:
                    marked = ""
                string = string + "{}{}".format(cell.value, marked) + " "
            print(string)
        print("")
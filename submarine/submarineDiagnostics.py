class submarineDiagnostics:
    def __init__(self):
        self.diagMask = []

        x = 1
        while(x <= 2048):
            self.diagMask.append(x)
            x = x*2
        
        self.diagMask.reverse()

        print("Diagnostics Mask:")
        print(self.diagMask)

        self.gammaRate              = 0
        self.epsilonRate            = 0
        self.powerConsumption       = 0
        self.oxygenGeneratorRating  = 0
        self.co2ScrubberRating      = 0
        self.rawDiagnostics         = []

    def readDiagnostics(self):
        self.__read_diagnostic_file()
        self.__calculateGammaRate()
        self.__calculateEpsilonRate()
        self.__calculatePowerConsumption()
        self.__calculateOxygenGeneratorRating()
        self.__calculateCO2ScrubberRating()
        self.__calculateLifeSupportRating()

    def __read_diagnostic_file(self):
        with open('inputFiles/day3_input.txt') as f:
            for x in f:
                self.rawDiagnostics.append(int(x, 2))
        f.close()
        # print("Raw Diagnostics:")
        # print(self.rawDiagnostics)

    def __calculateGammaRate(self):
        gammaString = ""
        for i in range(len(self.diagMask)):
            count = self.__countBitsMatchingMaskInList(self.diagMask[i], self.rawDiagnostics)
            if count > len(self.rawDiagnostics)/2:
                gammaString += "1"
            else:
                gammaString += "0"

        self.gammaRate = int(gammaString, 2)
        print("Gamma Rate: ", self.gammaRate, bin(self.gammaRate))

    def __countBitsMatchingMaskInList(self, mask, list):
        count = 0
        for item in list:
            if (item & mask) == mask:
                count += 1
        return count

    def __calculateEpsilonRate(self):
        self.epsilonRate = self.__bit_not(self.gammaRate)
        print("Epsilon Rate: ", self.epsilonRate, bin(self.epsilonRate))

    def __calculatePowerConsumption(self):
        self.powerConsumption = self.gammaRate * self.epsilonRate
        print("Power Consuption: ", self.powerConsumption)

    def __bit_not(self, n):
        return (1 << n.bit_length()) - 1 - n

    def __popularBitCounter(self, onesOrZeros):
        rawCopy = self.rawDiagnostics.copy()

        for i in range(len(self.diagMask)):
            if len(rawCopy) == 1:
                break
            # Determine the current bit criteria (which is more common, 1's or 0's)
            count = self.__countBitsMatchingMaskInList(self.diagMask[i], rawCopy)
            if count >= len(rawCopy)/2:#more 1's than 0's
                if onesOrZeros:
                    maskEquate = self.diagMask[i]#keep the on bits (1's)
                else:
                    maskEquate = 0#keep the off bits (0's)
            else:
                if onesOrZeros:
                    maskEquate = 0#keep the off bits (0's)
                else:
                    maskEquate = self.diagMask[i]#keep the on bits (1's)

            # loop rawCopy removing items that don't match the current
            # bit criteria that was determined above.
            j = 0
            rawLength = len(rawCopy)
            while j < rawLength:
                if rawCopy[j] & self.diagMask[i] != maskEquate:
                    rawCopy.remove(rawCopy[j])
                    rawLength = len(rawCopy)
                else:
                    j += 1

        return rawCopy[0]
        
    def __calculateOxygenGeneratorRating(self):
        self.oxygenGeneratorRating = self.__popularBitCounter(1)
        print("Oxygen Generator Rating:", self.oxygenGeneratorRating)

    def __calculateCO2ScrubberRating(self):
        self.co2ScrubberRating = self.__popularBitCounter(0)
        print("CO2 Scrubber Rating:", self.co2ScrubberRating)

    def __calculateLifeSupportRating(self):
        self.lifeSupportRating = self.co2ScrubberRating * self.oxygenGeneratorRating
        print("Life Support Rating:", self.lifeSupportRating)
class submarineDiagnostics:
    def __init__(self):
        self.diagMask = []

        x = 1
        while(x <= 4096):
            self.diagMask.append(x)
            x = x*2
        
        self.diagMask.reverse()

        print("Diagnostics Mask:")
        print(self.diagMask)

        self.gammaRate          = 0
        self.epsilonRate        = 0
        self.powerConsumption   = 0
        self.rawDiagnostics     = []

        self.read_diagnostic_file()
        self.calculateGammaRate()
        self.calculateEpsilonRate()
        self.calculatePowerConsumption()

    def read_diagnostic_file(self):
        with open('inputFiles/day3_input.txt') as f:
            for x in f:
                self.rawDiagnostics.append(int(x, 2))
        f.close()
        print("Raw Diagnostics:")
        print(self.rawDiagnostics)

    def calculateGammaRate(self):
        gammaString = ""
        for i in range(len(self.diagMask)):
            count = 0
            for j in range(len(self.rawDiagnostics)):
                if (self.rawDiagnostics[j] & self.diagMask[i]) == self.diagMask[i]:
                    count += 1
            if count > len(self.rawDiagnostics)/2:
                gammaString += "1"
            else:
                gammaString += "0"

        self.gammaRate = int(gammaString, 2)
        print("Gamma Rate: ", self.gammaRate, bin(self.gammaRate))

    def calculateEpsilonRate(self):
        self.epsilonRate = self.bit_not(self.gammaRate)
        print("Epsilon Rate: ", self.epsilonRate, bin(self.epsilonRate))

    def calculatePowerConsumption(self):
        self.powerConsumption = self.gammaRate * self.epsilonRate
        print("Power Consuption: ", self.powerConsumption)

    def bit_not(self, n):
        return (1 << n.bit_length()) - 1 - n
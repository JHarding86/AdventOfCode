from os import supports_dir_fd
from submarine.bingoSystem.bingoSystem import bingoSystem
from submarine.submarineCourse import submarineCourse
from submarine.submarineDiagnostics import submarineDiagnostics
from submarine.bingoSystem.bingoSystem import bingoSystem

class submarine:
    def __init__(self):
        self.depths                 = []
        self.slidingWindowDepths    = []

        self.submarineCourse        = submarineCourse()
        self.diagnostics            = submarineDiagnostics()
        self.bingo                  = bingoSystem()

        print("Submarine Initialized")

    def read_depths_input(self):
        with open('inputFiles/day1_input.txt') as f:
            for x in f:
                self.depths.append(int(x))
        f.close()

    def count_depth_increases(self, depths):
        res = 0
        for x in range(len(depths)):
            if x != 0:
                if depths[x] > depths[x-1]:
                    res += 1
        print(res)

    def sliding_window_depth_increase(self):
        count = 0
        index = 0
        innerCount = 0
        while(index < len(self.depths)):
            count += self.depths[index]
            if innerCount == 2:
                self.slidingWindowDepths.append(count)
                count = 0
                index -= 1
                innerCount = 0
            else:
                innerCount += 1
                index += 1
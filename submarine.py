class submarine:
    def __init__(self):
        self.depths = []
        self.slidingWindowDepths = []
        print("Submarine Initialized")

    def read_depths_input(self):
        with open('day1_input.txt') as f:
            for x in f:
                self.depths.append(int(x))
        f.close()

    # Day 1 part 1 Solution
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
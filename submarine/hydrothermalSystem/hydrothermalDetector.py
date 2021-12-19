from submarine.hydrothermalSystem.hydrothermalVent import hydrothermalVent

class hydrothermalDetector:
    def __init__(self):

        self.vents  = []
        self.map    = []
        self.maxX   = 0
        self.maxY   = 0
        
        self.__read_hydrothermals()
        self.__setupMap()
        # self.__printMap()

        # print(" ")

        self.__mapVents()
        # self.__printMap()

        self.__countOverlaps()
        print("Hydrothermal Detector Initialized")

    def __read_hydrothermals(self):
        with open('inputFiles/day5_input.txt') as f:
            for x in f:
                vent = hydrothermalVent(x)
                self.vents.append(vent)

                #track the size of the area we have mapped
                if vent.start[0] > self.maxX:
                    self.maxX = vent.start[0]
                if vent.end[0] > self.maxX:
                    self.maxX = vent.end[0]
                if vent.start[1] > self.maxY:
                    self.maxY = vent.start[1]
                if vent.end[1] > self.maxY:
                    self.maxY = vent.end[1]
        f.close()

    def __setupMap(self):
        for y in range(self.maxY+1):
            row = []
            for x in range(self.maxX+1):
                row.append(0)
                
            self.map.append(row)

    def __mapVents(self):
        for vent in self.vents:
            if vent.isVentHorizontal():
                self.__mapHorizontalVent(vent)
            elif vent.isVentVertical():
                self.__mapVerticalVent(vent)
            else:
                print("The vent is not vertical or horizontal, disregaurding it...")

    def __mapHorizontalVent(self, vent: hydrothermalVent):
        row = self.map[vent.start[1]]

        for i in range(vent.start[0], vent.end[0]+1):
            row[i] += 1

    def __mapVerticalVent(self, vent: hydrothermalVent):
        for y in range(vent.start[1], vent.end[1]+1):
            self.map[y][vent.start[0]] += 1

    def __countOverlaps(self):
        count = 0
        for row in self.map:
            for cell in row:
                if cell >= 2:
                    count += 1

        print("Hydrothernam Vent Overlaps:", count)

    def __printMap(self):
        for row in self.map:
            string = ""
            for cell in row:
                string = string + "{}".format(cell) + " "
            print(string)


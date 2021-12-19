class hydrothermalVent:
    def __init__(self, rawVentData):

        rawVentCoords       = rawVentData.split("->")
        start_map_object    = map(int, rawVentCoords[0].split(","))
        end_map_object      = map(int, rawVentCoords[1].split(","))
        self.start          = list(start_map_object)
        self.end            = list(end_map_object)

    def isVentVertical(self):
        if self.start[0] == self.end[0]:
            if self.start[1] > self.end[1]:
                temp            = self.end[1]
                self.end[1]     = self.start[1]
                self.start[1]   = temp
            return True
        else:
            return False

    def isVentHorizontal(self):
        if self.start[1] == self.end[1]:
            if self.start[0] > self.end[0]:
                temp            = self.end[0]
                self.end[0]     = self.start[0]
                self.start[0]   = temp
            return True
        else:
            return False
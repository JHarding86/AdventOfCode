from os import supports_dir_fd
from submarine.submarineCommand import submarineCommand
from submarine.submarineDiagnostics import submarineDiagnostics

class submarine:
    def __init__(self):
        self.depths                 = []
        self.slidingWindowDepths    = []
        self.plannedCourse          = []

        self.horizontalPosition     = 0
        self.depth                  = 0
        self.aim                    = 0

        self.diagnostics            = submarineDiagnostics()
        
        print("Submarine Initialized")

    def read_depths_input(self):
        with open('inputFiles/day1_input.txt') as f:
            for x in f:
                self.depths.append(int(x))
        f.close()

    def read_planned_course(self):
        with open('inputFiles/day2_input.txt') as f:
            for x in f:
                command = x.split(" ")
                subCmd = submarineCommand()
                subCmd.direction    = command[0]
                subCmd.distance     = int(command[1])
                self.plannedCourse.append(subCmd)
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

    def follow_planned_course(self):
        for cmd in self.plannedCourse:
            self.follow_command(cmd)

    def follow_command(self, cmd: submarineCommand):
        if cmd.direction == "forward":
            self.horizontalPosition += cmd.distance
            self.depth += self.aim * cmd.distance
        elif cmd.direction == "down":
            self.aim += cmd.distance
        elif cmd.direction == "up":
            self.aim -= cmd.distance
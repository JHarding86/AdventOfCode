from submarine.submarineCommand import submarineCommand

class submarineCourse:
    def __init__(self):
        self.plannedCourse          = []
        self.horizontalPosition     = 0
        self.depth                  = 0
        self.aim                    = 0

        print("Submarine Course Initialized")

    def executePlannedCourse(self):
        self.__read_planned_course()
        self.__follow_planned_course()
        print("Depth * Horizontal: ", self.horizontalPosition * self.depth)

    def __read_planned_course(self):
        with open('inputFiles/day2_input.txt') as f:
            for x in f:
                command = x.split(" ")
                subCmd = submarineCommand()
                subCmd.direction    = command[0]
                subCmd.distance     = int(command[1])
                self.plannedCourse.append(subCmd)
        f.close()

    def __follow_planned_course(self):
        for cmd in self.plannedCourse:
            self.__follow_command(cmd)

    def __follow_command(self, cmd: submarineCommand):
        if cmd.direction == "forward":
            self.horizontalPosition += cmd.distance
            self.depth += self.aim * cmd.distance
        elif cmd.direction == "down":
            self.aim += cmd.distance
        elif cmd.direction == "up":
            self.aim -= cmd.distance
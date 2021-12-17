from submarine.submarine import submarine

mySub = submarine()

mySub.read_depths_input()

#day 1 part one
print("Day 1 Part 1 Answer:")
mySub.count_depth_increases(mySub.depths)

#day 1 part two
print("Day 1 Part 2 Answer:")
mySub.sliding_window_depth_increase()
mySub.count_depth_increases(mySub.slidingWindowDepths)

#day 2
print("Day 2 Part 1 Answer: ")
mySub.submarineCourse.executePlannedCourse()

print("Day 3 Part 1 Answer:")
mySub.diagnostics.readDiagnostics()
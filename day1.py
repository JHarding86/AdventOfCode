from submarine import submarine

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
mySub.read_planned_course()
mySub.follow_planned_course()
print("Day 2 Part 1 Answer: ")
print(mySub.horizontalPosition * mySub.depth)
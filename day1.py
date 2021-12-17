from submarine import submarine

mySub = submarine()

mySub.read_depths_input()

#day 1 part one
mySub.count_depth_increases(mySub.depths)

#day 1 part two
mySub.sliding_window_depth_increase()
mySub.count_depth_increases(mySub.slidingWindowDepths)

lines = []
def open_read_lines():
    with open('day1_input.txt') as f:
        for x in f:
            lines.append(int(x))
    f.close()

# Day 1 part 1 Solution
def count_depth_increases(depths):
    res = 0
    for x, line in enumerate(depths):
        if x != 0:
            if depths[x] > depths[x-1]:
                res += 1
    print(res)

# Day 1 Part 2 Solution
def sliding_window_depth_increase(depths, slidingWindowDepths):
    count = 0
    index = 0
    innerCount = 0
    while(index < len(depths)):
        count += depths[index]
        if innerCount == 2:
            slidingWindowDepths.append(count)
            print(count)
            count = 0
            index -= 1
            innerCount = 0
        else:
            innerCount += 1
            index += 1

    # for x, line in enumerate(depths):
    #     count += line
    #     if (x+1) % 3 == 0:
    #         slidingWindowDepths.append(count)
    #         print(count)
    #         count = 0

open_read_lines()

# Day 1 Part 1
count_depth_increases(lines)

# Day 1 Part 2
slidingWindowDepths = []
sliding_window_depth_increase(lines, slidingWindowDepths)
count_depth_increases(slidingWindowDepths)
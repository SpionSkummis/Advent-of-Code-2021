import heapq as hq
import numpy as np

# FUNCTION DEFINITIONS

def adjacent(cave, coord):
    x, y = coord
    adj = set()
    for i in [-1,1]:
        if x + i >= 0 and x + i < cave.shape[1]:
            adj.add((x + i, y))
        if y + i >= 0 and y + i < cave.shape[0]:
            adj.add((x, y + i))
    return adj

def find_path(cave):
    done = False
    endpoint = (cave.shape[0] - 1, cave.shape[1] - 1)
    visited = set()
    paths = [(0, (0,0))]
    hq.heapify(paths)
    while not done:
        current = hq.heappop(paths)
        visited.add(current)
        next_steps = adjacent(cave, current[1]) - visited
        if(endpoint) in next_steps:
            done = True
            return current[0] + cave[endpoint]
            break
        for s in next_steps:
            hq.heappush(paths, (cave[s] + current[0], s))
            visited.add(s)


# INPUT

with open("inputs/day15.txt") as f:
    cave = np.array([[int(d) for d in l.strip()] for l in f.readlines()])

# PART ONE

res1 = find_path(cave)
    
print(f"Part 1: The lowest risk is {res1}")

# PART TWO

limit_vals = np.vectorize(lambda x: x if x <= 9 else x - 9)

cave2 = np.tile(cave, (5,5))
ones = np.ones(cave.shape, dtype=int)
for i in range(0,5):
    for j in range(0,5):
        cave2[cave.shape[0]*i:cave.shape[0]*(i+1),
              cave.shape[1]*j:cave.shape[1]*(j+1)] += ones*(i+j)

cave2 = limit_vals(cave2)

res2 = find_path(cave2)

print(f"Part 2: The lowest risk is {res2}")

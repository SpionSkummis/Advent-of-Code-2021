from functools import reduce
import numpy as np

with open("inputs/day09.txt") as f:
    height_map = np.array([[int(d) for d in l.strip()] for l in f.readlines()])

# PART ONE
ymax, xmax = height_map.shape

def adjacent(y, x):
    points = set()
    for i in [-1, 1]:
        if x+i != -1 and x+i != xmax:
            points.add((y, x+i))
        if y+i != -1 and y+i != ymax:
            points.add((y+i, x))
    return points

def low_point(p):
    return all([height_map[x] > height_map[p] for x in adjacent(*p)])

low_points = [(i, j) for i in range(0, ymax) for j in range(0, xmax) if low_point((i,j))]

risk_level = sum(height_map[p] for p in low_points) + len(low_points)

print(f"Part 1: The risk level is {risk_level}")

# PART TWO

def basin_size(lp):
    size = 0
    to_check = adjacent(*lp)
    checked = set()
    while len(to_check) > 0:
        p = to_check.pop()
        if not height_map[p] == 9:
            size += 1
            checked.add(p)
            to_check = to_check.union(adjacent(*p)) - checked
        else:
            checked.add(p)
    return size

basin_sizes = [basin_size(p) for p in low_points]
basin_sizes.sort()
res2 = reduce(lambda a, b: a*b, basin_sizes[-3:])

print(f"Part 2: The product of the three largest basins is {res2}")

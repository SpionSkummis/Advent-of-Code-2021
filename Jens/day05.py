import re

with open("inputs/day05.txt") as f:
    data = [re.findall("\d+", l) for l in f.readlines()]
    data = [[(int(d[0]), int(d[1])), (int(d[2]), int(d[3]))] for d in data]

def crack_range(c1, c2, diags = False):
    if c1[0] == c2[0]:
        rng = [(c1[0], y)
                for y in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1)]
        return rng
    elif c1[1] == c2[1]:
        rng = [(x, c1[1])
                for x in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1)]
        return rng
    elif diags:
        xdir = 1 if c1[0] < c2[0] else -1
        xrng = range(c1[0], c2[0] + xdir, xdir)
        ydir = 1 if c1[1] < c2[1] else -1
        yrng = range(c1[1], c2[1] + ydir, ydir)
        return list(zip(xrng, yrng))

# PARTS 1 AND 2

cracks_map1 = {}
cracks_map2 = {}

for d in data:
    if d[0][0] == d[1][0] or d[0][1] == d[1][1]:
        for c in crack_range(d[0], d[1]):
            if c in cracks_map1:
                cracks_map1[c] += 1
            else:
                cracks_map1[c] = 1
            if c in cracks_map2:
                cracks_map2[c] += 1
            else:
                cracks_map2[c] = 1
    else:
        for c in crack_range(d[0], d[1], True):
            if c in cracks_map2:
                cracks_map2[c] += 1
            else:
                cracks_map2[c] = 1

res1 = len(list(filter(lambda x: x > 1, cracks_map1.values())))
print(f"Part 1: The number of overlapping squares is {res1}")

res2 = len(list(filter(lambda x: x > 1, cracks_map2.values())))
print(f"Part 2: The number of overlapping squares is {res2}")

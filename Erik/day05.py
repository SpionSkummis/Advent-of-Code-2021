import numpy as np

data = []
with open("Erik/inputs/input05.txt", "r") as f:
    for line in f:
        temp = line.strip().split(" -> ")
        temp = [[int(x) for x in temp[0].split(",")], [int(y) for y in temp[1].split(",")]]
        data.append(temp)

x_max = 1000
y_max = 1000

grid = np.zeros((x_max, y_max))
grid2 = np.zeros((x_max, y_max))

for instr in data:
    x1, y1 = instr[0]
    x2, y2 = instr[1]
    if (x1 == x2):
        for y in range(min(y1, y2), max(y1, y2)+1):
            grid[x1][y] += 1
            grid2[x1][y] += 1
    elif (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2)+1):
            grid[x][y1] += 1
            grid2[x][y1] += 1
    else:
        if x1 < x2:
            x_vals = [a for a in range(x1, x2+1)]
        else:
            x_vals = [a for a in range(x1, x2-1, -1)]
        if y1 < y2:
            y_vals = [a for a in range(y1, y2+1)]
        else:
            y_vals = [a for a in range(y1, y2-1, -1)]
        for i in range(len(x_vals)):
            grid2[x_vals[i]][y_vals[i]] += 1

mult_vent_count = 0
mult_vent_count2 = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] > 1:
            mult_vent_count += 1
        if grid2[x][y] > 1:
            mult_vent_count2 += 1

print(f"Part 1: {mult_vent_count}")
print(f"Part 2: {mult_vent_count2}")

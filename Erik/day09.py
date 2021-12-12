#1588 too high
import numpy as np
with open("Erik/inputs/input09.txt", "r") as f:
    heatmap = np.array([[int(y) for y in x.strip()] for x in f.readlines()])

def check_for_lower(x, y, inmap):
    if x == 0:
        if (inmap[x+1][y] <= inmap[x][y]):
            return True
    elif x == len(inmap) - 1:
        if (inmap[x-1][y] <= inmap[x][y]):
            return True
    else:
        if (inmap[x+1][y] <= inmap[x][y]) or (inmap[x-1][y] <= inmap[x][y]):
            return True
    if y == 0:
        if (inmap[x][y+1] <= inmap[x][y]):
            return True
    elif y == len(inmap[0]) -1:
        if (inmap[x][y-1] <= inmap[x][y]):
            return True
    else:
        if (inmap[x][y+1] <= inmap[x][y]) or (inmap[x][y-1] <= inmap[x][y]):
            return True
    return False

def find_base_size(start_coords, inmap, all_coords):
    x = start_coords[0]
    y = start_coords[1]
    all_coords.add((x,y))
    temp_coord_set = set()

    if x < (len(inmap) -1):
        if (inmap[x+1][y] < 9):
            temp_coord_set.add((x+1,y))
    if x > 0:
        if (inmap[x-1][y] < 9):
            temp_coord_set.add((x-1,y))
    
    if y < (len(inmap[0]) -1):
        if (inmap[x][y+1] < 9):
            temp_coord_set.add((x,y+1))
    if y > 0:
        if (inmap[x][y-1] < 9):
            temp_coord_set.add((x,y-1))
    
    if len(all_coords.difference(temp_coord_set)) == 0:
        return all_coords
    for coord in temp_coord_set.difference(all_coords):
        all_coords.update(find_base_size(coord, inmap, all_coords))

    return all_coords

risk_level = 0
low_coordinates = []
for x_pos in range(len(heatmap)):
    for y_pos in range(len(heatmap[0])):
        if not check_for_lower(x_pos, y_pos, heatmap):
            risk_level += heatmap[x_pos][y_pos] + 1
            low_coordinates.append((x_pos, y_pos))


print("Part 1:", risk_level)

all_regions = []
for coord in low_coordinates:
    all_regions.append(find_base_size(coord, heatmap, set()))
bignum = sorted([len(x) for x in all_regions])

print(f"Part 2: {bignum[-1]*bignum[-2]*bignum[-3]}")

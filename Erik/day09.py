#1588 too high
import numpy as np
with open("Erik/inputs/input09-t.txt", "r") as f:
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

def find_base_size(start_coords, inmap, all_coords=set()):
    x = start_coords[0]
    y = start_coords[1]
    go_deeper = False
    temp_coord_set = set()


    if x == 0:
        if (inmap[x+1][y] < 9):
                temp_coord_set.add((x+1,y))
    elif x == len(inmap) - 1:
            if (inmap[x-1][y] < 9):
                temp_coord_set.add((x-1,y))
    else:
        if (inmap[x+1][y] < 9):
                temp_coord_set.add((x+1,y))
        if (inmap[x-1][y] < 9):
                temp_coord_set.add((x-1,y))
    if y == 0:
        if (inmap[x][y+1] < 9):
                temp_coord_set.add(inmap[(x+1,y)])
    elif y == len(inmap[0]) -1:
        if (inmap[x][y-1] == 9):
                temp_coord_set.add(inmap[(x+1,y)])
    else:
        if (inmap[x][y+1]== 9) or (inmap[x][y-1] == 9):
                temp_coord_set.add(inmap[(x+1,y)])
    return go_deeper


    return all_coords



risk_level = 0
low_coordinates = []
for x_pos in range(len(heatmap)):
    for y_pos in range(len(heatmap[0])):
        if not check_for_lower(x_pos, y_pos, heatmap):
            risk_level += heatmap[x_pos][y_pos] + 1
            low_coordinates.append((x_pos, y_pos))


print("Part 1:", risk_level)

print(low_coordinates)

print(find_base_size(low_coordinates[0], heatmap))
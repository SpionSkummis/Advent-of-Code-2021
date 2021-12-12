with open("inputs/day11.txt") as f:
    c = [[int(d) for d in x.strip()] for x in f.readlines()]
    starting_cave = {(i,j): c[i][j] for i in range(0,len(c)) for j in range(0,len(c[0]))}

def adjacent(coord):
    x_lower = coord[0]-1 if coord[0] != 0 else coord[0]
    x_upper = coord[0]+1 if coord[0] != 9 else coord[0]
    y_lower = coord[1]-1 if coord[1] != 0 else coord[1]
    y_upper = coord[1]+1 if coord[1] != 9 else coord[1]
    return {(x, y) for x in range(x_lower, x_upper+1)
            for y in range(y_lower, y_upper+1)} - {coord}
    
def flash(cave, coord):
    for c in adjacent(coord):
        cave[c] += 1

def step(cave):
    already_flashed = set()
    for c in cave:
        cave[c] += 1
    ready_to_flash = {c for c in cave if cave[c] > 9}
    while ready_to_flash != already_flashed:
        for c in ready_to_flash - already_flashed:
            flash(cave, c)
        already_flashed = already_flashed.union(ready_to_flash)
        ready_to_flash = {c for c in cave if cave[c] > 9}
    for c in already_flashed:
        cave[c] = 0
    return already_flashed
    
# PART ONE

flashes = 0
cave = starting_cave.copy()
for _ in range(100):
    flashes += len(step(cave))
    
print(f"Part 1: The number of flashes after 100 steps is {flashes}.")

# PART TWO

steps = 0
all_flash = False
cave = starting_cave.copy()
while not all_flash:
    steps += 1
    flashing = step(cave)
    if len(flashing) == 100:
        all_flash = True

print(f"Part 2: All octopuses flash after {steps} steps.")

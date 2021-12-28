import numpy as np

with open("Erik/inputs/input11.txt", "r") as f:
    octo = np.array([[int(x) for x in y.strip()] for y in f.readlines()])

def take_step(octo_grid):
    in_grid = octo_grid.copy()
    can_flash = np.ones((len(in_grid), len(in_grid[0])), dtype=int)
    in_grid += 1
    more_rounds = True
    while(more_rounds):
        more_rounds = False
        for x in range(len(in_grid)):
            for y in range(len(in_grid[0])):
                if (in_grid[x][y] > 9) and can_flash[x][y]:
                    can_flash[x][y] = 0
                    xmin = x-1 if x > 0 else x
                    xmax = x+2 if x != len(in_grid) else x+1
                    ymin = y-1 if y > 0 else y
                    ymax = y+2 if y != len(in_grid[0]) else y+1
                    in_grid[xmin:xmax,ymin:ymax] += 1
                    more_rounds = True
    flash_counter = 0
    for x in range(len(in_grid)):
            for y in range(len(in_grid[0])):
                if in_grid[x][y] > 9:
                    in_grid[x][y] = 0
                    flash_counter += 1
    return in_grid, flash_counter


# Part 1:
grid = octo.copy()
steps = 100
flashes = 0
for _ in range(steps):
    grid, tempcount = take_step(grid)
    flashes += tempcount
print(f"Flashes after {steps} steps: {flashes}")


#Part 2:
grid2 = octo.copy()
octo_num = len(octo) * len(octo[0])
rounds = 0
keep_running = True
while(keep_running):
    rounds += 1
    grid2, tempcount = take_step(grid2)
    if tempcount == octo_num:
        keep_running = False

print(f"All octopuses will flash at the same time after {rounds} rounds")

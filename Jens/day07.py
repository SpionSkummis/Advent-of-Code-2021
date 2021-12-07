import numpy as np

with open("inputs/day07.txt") as f:
    positions = np.array([int(d) for d in f.readline().split(",")])

# PART ONE
    
rng = np.array(range(min(positions), max(positions) + 1))
distances = np.abs(np.tile(positions, (len(rng), 1)).T - rng)
fuel_spent = np.sum(distances, axis=0)

res1 = np.min(fuel_spent)
print(f"Part 1: The least amount of fuel spent is {res1}")

# PART TWO

def dist_to_fuel(d):
    return d * (1 + d) // 2

fuel_spent = np.sum(np.vectorize(dist_to_fuel)(distances), axis=0)

res2 = np.min(fuel_spent)
print(f"Part 2: The least amount of fuel spent is {res2}")

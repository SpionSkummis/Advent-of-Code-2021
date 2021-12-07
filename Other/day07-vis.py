import statistics
import matplotlib.pyplot as plt

with open("Erik/inputs/input07.txt", "r") as f:
    crabsubs = [int(x) for x in f.read().strip().split(",")]

crab_median = statistics.median(crabsubs)
crab_mean = round(statistics.mean(crabsubs))

def calc_fuel(in_list, final_pos):
    return int(sum([abs(final_pos - x) for x in in_list]))

def calc_fuel3(in_list, final_pos):
    return int(sum([(abs(final_pos-x) * (abs(final_pos-x)+1)) / 2 for x in in_list]))
    
part1 = calc_fuel(crabsubs, crab_median)
print(f"Part 1 total fuel usage: {part1}")

part2 = min([calc_fuel3(crabsubs, x) for x in range(crab_mean-7, crab_mean+8)])
print(f"Part 2 total fuel usage: {part2}")

#bruteforce

crab_range = range(min(crabsubs), max(crabsubs)+1)
first_fuel = [calc_fuel(crabsubs, x) for x in crab_range]
all_fuel = [calc_fuel3(crabsubs, x) for x in crab_range]


fig, ax = plt.subplots()
ax.plot(crab_range, first_fuel, color="green")
ax.set(xlim=(min(crabsubs), max(crabsubs)),ylim=(0,max(first_fuel)))
plt.show()


fig, ax = plt.subplots()
ax.plot(crab_range, all_fuel)#, width=1)
ax.set(xlim=(min(crabsubs), max(crabsubs)),ylim=(0,max(all_fuel)))
plt.show()

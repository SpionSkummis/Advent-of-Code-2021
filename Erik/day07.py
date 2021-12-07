import statistics
with open("Erik/inputs/input07.txt", "r") as f:
    crabsubs = [int(x) for x in f.read().strip().split(",")]

crab_median = statistics.median(crabsubs)
crab_mean = round(statistics.mean(crabsubs))

def calc_fuel(in_list, final_pos):
    return int(sum([abs(final_pos - x) for x in in_list]))

def calc_fuel2(in_list, final_pos):
    #Den här funktionen får stå kvar så att jag får skämmas
    return sum([sum(range(abs(final_pos-x)+1)) for x in in_list])
    #Eller om man vill kunna läsa det:
    #crab_ranges = [range(abs(final_pos-x)+1)) for x in in_list]
    #return sum([sum(x) for x in crab_ranges])

def calc_fuel3(in_list, final_pos):
    return int(sum([(abs(final_pos-x) * (abs(final_pos-x)+1)) for x in in_list])/2)
    
    
part1 = calc_fuel(crabsubs, crab_median)
print(f"Part 1 total fuel usage: {part1}")

part2 = min([calc_fuel3(crabsubs, x) for x in range(crab_mean-2, crab_mean+3)])
print(f"Part 2 total fuel usage: {part2}")

#bruteforce
"""
all_fuel = [calc_fuel2(crabsubs, x) for x in range(min(crabsubs), max(crabsubs)+1)]
print(min(all_fuel))
"""

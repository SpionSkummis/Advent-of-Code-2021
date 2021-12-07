import statistics
with open("Erik/inputs/input07.txt", "r") as f:
    crabsubs = [int(x) for x in f.read().strip().split(",")]

crab_median = statistics.median(crabsubs)
crab_mean = round(statistics.mean(crabsubs))

def calc_fuel(in_list, final_pos):
    return int(sum([abs(final_pos - x) for x in in_list]))

def calc_fuel2(in_list, final_pos):
    #Den här funktionen löser en bruteforce på ca 21 sekunder på en inkopplad laptop
    return sum([sum(range(abs(final_pos-x)+1)) for x in in_list])
    #Eller om man vill kunna läsa det:
    #crab_ranges = [range(abs(final_pos-x)+1)) for x in in_list]
    #return sum([sum(x) for x in crab_ranges])

def calc_fuel3(in_list, final_pos):
    #Den här funktionen löser en bruteforce på ca 0.52 sekunder på en inkopplad laptop
    return int(sum([(abs(final_pos-x) * (abs(final_pos-x)+1)) / 2 for x in in_list]))

def calc_fuel4(in_list, final_pos):
    #Den här funktionen löser en bruteforce på ca 0.46 sekunder på en inkopplad laptop
    return int(sum([(abs(final_pos-x) * (abs(final_pos-x)+1)) for x in in_list])/2)

def calc_fuel5(in_list, final_pos):
    #Den här funktionen löser en bruteforce på ca 0.78 sekunder på en inkopplad laptop
    return int(sum([abs(final_pos-x)**2 + abs(final_pos-x) for x in in_list])/2)

def calc_fuel6(in_list, final_pos):
    #Den här funktionen löser en bruteforce på ca 0.72 sekunder på en inkopplad laptop
    return int(sum([(final_pos-x)**2 + abs(final_pos-x) for x in in_list])/2)

part1 = calc_fuel(crabsubs, crab_median)
print(f"Part 1 total fuel usage: {part1}")

part2 = min([calc_fuel2(crabsubs, x) for x in range(crab_mean-1, crab_mean+2)])
print(f"Part 2 total fuel usage: {part2}")
part3 = min([calc_fuel3(crabsubs, x) for x in range(crab_mean-1, crab_mean+2)])
print(f"Part 3 total fuel usage: {part2}")
part4 = min([calc_fuel4(crabsubs, x) for x in range(crab_mean-1, crab_mean+2)])
print(f"Part 4 total fuel usage: {part2}")
part5 = min([calc_fuel5(crabsubs, x) for x in range(crab_mean-1, crab_mean+2)])
print(f"Part 5 total fuel usage: {part2}")
part5 = min([calc_fuel6(crabsubs, x) for x in range(crab_mean-1, crab_mean+2)])
print(f"Part 6 total fuel usage: {part2}")

#bruteforce
"""
all_fuel = [calc_fuel2(crabsubs, x) for x in range(min(crabsubs), max(crabsubs)+1)]
print(min(all_fuel))
"""

import timeit

#För långsam för att få vara med och leka
#print(timeit.timeit(lambda:[calc_fuel2(crabsubs, x) for x in range(min(crabsubs), max(crabsubs)+1)],number=1))
print(timeit.timeit(lambda:[calc_fuel3(crabsubs, x) for x in range(min(crabsubs), max(crabsubs)+1)],number=10))
print(timeit.timeit(lambda:[calc_fuel4(crabsubs, x) for x in range(min(crabsubs), max(crabsubs)+1)],number=10))
print(timeit.timeit(lambda:[calc_fuel5(crabsubs, x) for x in range(min(crabsubs), max(crabsubs)+1)],number=10))
print(timeit.timeit(lambda:[calc_fuel6(crabsubs, x) for x in range(min(crabsubs), max(crabsubs)+1)],number=10))

print('Advent of Code 2021 - December 07 - Olof')
crabPositions = [int(a) for a in open('Olof\day07_input.txt','r').read().split(',')]
lowestFuelCost, lowestFuelCost2 = 99999999999999999, 99999999999999999

for position in range(min(crabPositions), max(crabPositions)+1):
    fuelCost, fuelCost2 = 0, 0
    for crab in crabPositions:
        fuelCost += abs(crab-position)
        fuelCost2 += ((1 + abs(crab-position)) * abs(crab-position) / 2)
    if fuelCost < lowestFuelCost:
        lowestFuelCost = fuelCost
    if fuelCost2 < lowestFuelCost2:
        lowestFuelCost2 = fuelCost2

print('Part 1: ' + str(lowestFuelCost) + '\nPart 2: ' + str(int(lowestFuelCost2)))
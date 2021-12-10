print('Advent of Code 2021 - December 01 - Olof')
inputList = list(open('Olof\day01_input.txt','r').read().splitlines())

part1_counter = 0
for i in range(1, len(inputList)):
    if int(inputList[i]) > int(inputList[i-1]):
        part1_counter += 1

part2_counter = 0
for i in range(3, len(inputList)):
    sum_current = int(inputList[i]) + int(inputList[i-1]) + int(inputList[i-2])
    sum_previous = int(inputList[i-1]) + int(inputList[i-2]) + int(inputList[i-3])
    if sum_current > sum_previous:
        part2_counter += 1

print('Part 1: ' + str(part1_counter))
print('Part 2: ' + str(part2_counter))
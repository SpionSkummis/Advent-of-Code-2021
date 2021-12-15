print('Advent of Code 2021 - December 06 - Olof')

fishState = [0]*9
for fish in [int(a) for a in open('Olof\day06_input.txt','r').read().split(',')]:
    fishState[fish] += 1

for day in range(1, 256+1):
    nextFishState = [0]*9
    for i in range(1, 9):
        nextFishState[i-1] += fishState[i]
    nextFishState[6] += fishState[0]
    nextFishState[8] += fishState[0]
    fishState = nextFishState
    if day == 80:
        print('Part 1: ' + str(sum(fishState)))
print('Part 2: ' + str(sum(fishState)))
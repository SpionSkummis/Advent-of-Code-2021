import numpy as np

print('Advent of Code 2021 - December 11 - Olof')
input = np.array([list(a) for a in list(open('Olof\day11_input.txt','r').read().splitlines())]).astype(int)
input = np.pad(input, 1)
row, col = input.shape
flashCount, stepCount = 0, 0

while True:
    input[1:-1, 1:-1] += 1
    flashedLastRound = 1
    while flashedLastRound > 0:
        flashedLastRound = 0
        for r in range(1, row-1):
            for c in range(1, col-1):
                if input[r,c] > 9:
                    input[r,c] = -999999
                    input[r-1:r+2, c-1:c+2] += 1
                    flashedLastRound += 1
    
    flashCount += np.count_nonzero(input[1:-1, 1:-1] < 0)
    input[input < 0] = 0
    
    stepCount += 1
    if stepCount == 100:
        print('Part 1: ' + str(flashCount))

    if np.count_nonzero(input[1:-1, 1:-1]) == 0:
        print('Part 2: ' + str(stepCount))
        break
import numpy as np

print('Advent of Code 2021 - December 03 - Olof')
input = np.array([list(a) for a in list(open('Olof\day03_input_test.txt','r').read().splitlines())])

gam, eps = '',''
for i in range(len(input[0])):
    if np.count_nonzero(input[:,i] == '1') > np.count_nonzero(input[:,i] == '0'):
        gam += '1'
        eps += '0'
    else:
        gam += '0'
        eps += '1'
print('Part 1: ' + str(int(gam,2) * int(eps,2)))

oxygen = input.copy()
col = 0
while len(oxygen) > 1:
    ones = oxygen[np.where(oxygen[:, col]=='1')]
    zeros = oxygen[np.where(oxygen[:, col]=='0')]
    col += 1
    if len(ones) >= len(zeros):
        oxygen = ones
    else:
        oxygen = zeros

co2 = input.copy()
col = 0
while len(co2) > 1:
    ones = co2[np.where(co2[:, col]=='1')]
    zeros = co2[np.where(co2[:, col]=='0')]
    col += 1
    if len(zeros) <= len(ones):
        co2 = zeros
    else:
        co2 = ones
print('Part 2: ' + str(int(''.join(oxygen[0].tolist()), 2) * int(''.join(co2[0].tolist()), 2)))
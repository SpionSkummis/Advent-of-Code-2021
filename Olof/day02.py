print('Advent of Code 2021 - December 02 - Olof')
input = list(open('Olof\day02_input.txt','r').read().splitlines())
h, d, h2, d2, a= 0, 0,0,0,0

for s in input:
    instr = s.split()[0]
    x = int(s.split()[1])

    if instr == 'forward':
        h += x
        h2 += x
        d2 += (a * x)
    elif instr == 'down':
        a += x
        d += x
    elif instr == 'up':
        d -= x
        a -= x
print('Part 1: ' + str(h*d))
print('Part 2: ' + str(h2*d2))

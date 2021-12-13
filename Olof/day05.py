import numpy as np, re
print('Advent of Code 2021 - December 05 - Olof')

lines = []
for l in open('Olof\day05_input.txt','r').read().splitlines():
    f = [int(a) for a in re.split(' -> |,',l)]
    lines.append((int(f[0]), int(f[1]), int(f[2]), int(f[3])))

points1 = dict()
points2 = dict()

# def printdict(): #används bara under test, sen blir det lite stort...
#     print('\n')
#     for y in range(10):
#         xstr = ''
#         for x in range(10):
#             if (x,y) in points2:
#                 xstr += str(points2[(x,y)])
#             else:
#                 xstr += '.'
#         print(xstr)

for i in range(len(lines)): 
    x1, y1, x2, y2 = lines[i]
    xstep = 1 if x2 >= x1 else -1
    ystep = 1 if y2 >= y1 else -1
    if x1 == x2 or y1 == y2: #horizontal + vertical lines
        for y in range(y1, y2+ystep, ystep):
            for x in range(x1, x2+xstep, xstep):
                points1[(x,y)] = points1[(x,y)] + 1 if (x,y) in points1 else 1
                points2[(x,y)] = points2[(x,y)] + 1 if (x,y) in points2 else 1
    else: #diagonal lines
        x = x1
        for y in range(y1, y2+ystep, ystep):
            points2[(x,y)] = points2[(x,y)] + 1 if (x,y) in points2 else 1
            x += xstep
print('Part 1: ' + str(len([v for v in points1.values() if int(v) > 1])))
print('Part 2: ' + str(len([v for v in points2.values() if int(v) > 1])))
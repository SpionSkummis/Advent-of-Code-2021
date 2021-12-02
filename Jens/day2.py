import re

with open("inputs/day2.txt") as f:
    instructions = [(re.search("[a-z]+", l).group(),
                     int(re.search("[0-9]+", l).group()))
                    for l in f.readlines()]

# PART 1
hor = 0
vert = 0
for i in instructions:
    if i[0] == "up":
        vert -= i[1]
    elif i[0] == "down":
        vert += i[1]
    else:
        hor += i[1]

res1 = hor * vert

print(f"Part 1: The product is {res1}.")

# PART 2
hor = 0
vert = 0
aim = 0
for i in instructions:
    if i[0] == "up":
        aim -= i[1]
    elif i[0] == "down":
        aim += i[1]
    else:
        hor += i[1]
        vert += i[1] * aim

res2 = hor * vert

print(f"Part 2: The product is {res2}.")

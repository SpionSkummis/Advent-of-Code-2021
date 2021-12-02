directions = []
with open("Erik/inputs/input02.txt", "r") as f:
    for line in f:
        directions.append(line.strip())


depth = 0
pos = 0

aim = 0
depth_two = 0

for instr in directions:
    val = int(instr.split(" ")[1])
    if "up" in instr:
        depth -= val
        aim -= val
    elif "down" in instr:
        depth += val
        aim += val
    elif "forward" in instr:
        pos += val
        depth_two += aim * val

print(depth, pos, depth*pos)
print(depth_two, pos, depth_two * pos)
directions = []
with open("Erik/inputs/input02.txt", "r") as f:
    for line in f:
        directions.append(line.strip())

depth = 0 #Kommer alltid att ha samma värde som "aim"
pos = 0

depth_two = 0

for instr in directions:
    val = int(instr.split(" ")[1])
    if "up" in instr:
        depth -= val
    elif "down" in instr:
        depth += val
    elif "forward" in instr:
        pos += val
        depth_two += depth * val

print(f"Part 1: Curren depth is {depth} and current horizontal position is {pos}. Answer: {depth*pos}")
print(f"Part 2: Curren depth is {depth_two} and current horizontal position is {pos}. Answer: {depth_two*pos}")

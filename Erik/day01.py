# Read data as list of ints
depth_list = []
with open("Erik/inputs/input01.txt", "r") as f:
    for line in f:
        depth_list.append(int(line))

# Part 1
deeper_count = 0
for i in range(0,len(depth_list)-1):
    if depth_list[i] < depth_list[i+1]:
        deeper_count += 1
print(f"Part 1: {deeper_count}")

# Part 2
deeper_range_count = 0
for i in range(0,len(depth_list)-3):
    if sum(depth_list[i:i+3]) < sum(depth_list[i+1:i+4]):
        deeper_range_count += 1
print(f"Part 2: {deeper_range_count}")

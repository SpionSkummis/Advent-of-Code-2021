with open("inputs/day1.txt") as f:
    data = [int(d) for d in f.readlines()]

# PART 1
res1 = sum(data[i] < data[i+1] for i in range(len(data) - 1))

print(f"Part 1: The depth increases {res1} times.\n")

# PART 2
res2 = sum(sum(data[i:i+3]) < sum(data[i+1:i+4]) for i in range(len(data) - 3))

print(f"Part 2: The depth increases {res2} times.\n")

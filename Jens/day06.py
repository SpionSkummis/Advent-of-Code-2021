from collections import Counter

with open("inputs/day06.txt") as f:
    data = [int(d) for d in f.readline().split(",")]

# PARTS ONE AND TWO

def count_fish(fish, end):
    c = {x: 0 for x in range(0,10)}
    c.update(Counter(fish))
    tally = sum(c.values())
    for j in range(1, end + 1):
        c[7] += c[0]
        c[9] += c[0]
        tally += c[0]
        for i in range(1, 10):
            c[i-1] = c[i]
        c[9] = 0
    return tally

res1 = count_fish(data, 80)
print(f"Part one: The number of fish after 80 days is {res1}")

res2 = count_fish(data, 256)
print(f"Part two: The number of fish after 256 days is {res2}")


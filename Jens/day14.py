from collections import Counter

with open("inputs/day14.txt") as f:
    starting_polymer = f.readline().strip()
    insertion_data = [l.strip().split(" -> ") \
                      for l in f.readlines() if l.strip()]
    insertions = {r[0]: {r[0][0] + r[1], r[1] + r[0][1]} for r in insertion_data}
    starting_pairs = [starting_polymer[i] + starting_polymer[i+1] \
        for i in range(len(starting_polymer) - 1)]
    starting_pair_count = {r[0]: 0 for r in insertion_data}
    for p in starting_pairs:
        starting_pair_count[p] += 1

def count_letters(pair_count):
    letter_count = {c: 0 for c in "".join(insertions.keys())}
    for l in letter_count:
        for k in pair_count:
            for c in k:
                if c == l:
                    letter_count[l] += pair_count[k]
        if l == starting_polymer[0] or l == starting_polymer[-1]:
            letter_count[l] += 1
        letter_count[l] //= 2
    return letter_count

def step(pair_count):
    new_pair_count = {p: 0 for p in pair_count}
    for p in pair_count:
        for k in insertions[p]:
            new_pair_count[k] += pair_count[p]
    return new_pair_count

# PART ONE
pair_count = starting_pair_count.copy()
for _ in range(0, 10):
    pair_count = step(pair_count)

letter_count = count_letters(pair_count)
res1 = max(letter_count.values()) - min(letter_count.values())
print(f"Part 1: The difference is {res1}.")

# PART TWO

pair_count = starting_pair_count.copy()
for _ in range(0, 40):
    pair_count = step(pair_count)

letter_count = count_letters(pair_count)
res2 = max(letter_count.values()) - min(letter_count.values())
print(f"Part 2: The difference is {res2}")

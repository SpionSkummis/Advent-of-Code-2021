import numpy as np

with open("inputs/day03test.txt") as f:
    data = np.array([list(l.strip()) for l in f.readlines()]).astype(int)

# PART 1

total_cols = len(data[0])
pwrs2 = np.array([2**(total_cols - i - 1) for i in np.arange(total_cols)])

def calc_gamma(d):
    col_sums = np.sum(d, axis=0)
    cols = len(col_sums)
    rows = len(d)
    return pwrs2 @ (col_sums >= (rows / 2))
               
    
gamma = calc_gamma(data)
epsilon = ~gamma & 2**total_cols - 1

res1 = gamma * epsilon
print(f"Part 1: The power consumption is {res1}.")

# PART 2

def filter_fn(d, mask, i):
    return d[i] == mask >> (total_cols - i - 1) & 1

o2_data = co2_data = data
for i in range(total_cols):
    if len(o2_data) > 1:
        gamma = calc_gamma(o2_data)
        o2_data = list(filter(lambda x: filter_fn(x, gamma, i), o2_data))
    if len(co2_data) > 1:
        epsilon = ~calc_gamma(co2_data) & 2**total_cols - 1
        co2_data = list(filter(lambda x: filter_fn(x, epsilon, i), co2_data))
    if len(o2_data) == len(co2_data) == 1:
        break

res2 = o2_data[0] @ pwrs2 * co2_data[0] @ pwrs2
print(f"Part 2: The life support rating is {res2}.")

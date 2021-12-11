with open("inputs/day08.txt") as f:
    lines = [d.split("|") for d in f.readlines()]
    signals = [l[0].split() for l in lines]
    displays = [l[1].split() for l in lines]
    
# PART ONE

output_lens = [len(x) for d in displays for x in d]
res1 = sum(x in {2, 3, 4, 7} for x in output_lens)
print(f"Part 1: The number of uniquely identifiable digits is {res1}")

# PART TWO

res2 = 0
for i in range(len(signals)):
    signal_map = [0]*10
    unidentified = [set(c for c in x) for x in signals[i]]
    display = [set(c for c in x) for x in displays[i]]

    for c in unidentified:
        if len(c) == 2:
            signal_map[1] = c
        elif len(c) == 3:
            signal_map[7] = c
        elif len(c) == 4:
            signal_map[4] = c
        elif len(c) == 7:
            signal_map[8] = c

    for c in [c for c in unidentified if len(c) == 6]:
        if not signal_map[1] < c:
            signal_map[6] = c
        elif signal_map[4] < c:
            signal_map[9] = c
        else:
            signal_map[0] = c

    for c in [c for c in unidentified if len(c) == 5]:
        if not c < signal_map[9]:
            signal_map[2] = c
        elif signal_map[1] < c:
            signal_map[3] = c
        else:
            signal_map[5] = c

    output = 0
    for i in range(len(display)):
        output += signal_map.index(display[i]) * 10**(len(display)-i-1)

    res2 += output

print(f"Part 2: The sum of all outputs is {res2}")

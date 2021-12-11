import math

with open("inputs/day10.txt") as f:
    lines = [l.strip() for l in f.readlines()]

closing = {")": "(",
           "]": "[",
           "}": "{",
           ">": "<"}

def find_corrupt(line):
    opening = []
    for c in line:
        if c in closing:
            if opening[-1] != closing[c]:
                return c
            else:
                opening.pop()
        else:
            opening.append(c)
    return False

# PART ONE

scores = {")": 3,
          "]": 57,
          "}": 1197,
          ">": 25137}

score = 0
for l in lines:
    corrupt = find_corrupt(l)
    if corrupt:
        score += scores[corrupt]

print(f"Part 1: The score is {score}")

# PART TWO

incomplete_lines = [l for l in lines if not find_corrupt(l)]

scores2 = {")": 1,
           "]": 2,
           "}": 3,
           ">": 4}

completion = {"(": ")",
              "[": "]",
              "{": "}",
              "<": ">"}

def complete(line):
    opening = []
    for c in line:
        if c in closing:
            opening.pop()
        else:
            opening.append(c)
    return [completion[x] for x in opening]

score2 = []
for l in incomplete_lines:
    score2.append(0)
    comp_parens = complete(l)
    comp_parens.reverse()
    for c in comp_parens:
        score2[-1] *= 5
        score2[-1] += scores2[c]

score2.sort()
res2 = score2[math.floor(len(score2)/2)]
print(f"Part 2: The score is {res2}")

import numpy as np

with open("inputs/day13.txt") as f:
    dot_data, fold_data = f.read().split("\n\n")
    xsize = 0
    ysize = 0

    fold_dirs = []
    for d in fold_data.strip().split("\n"):
        direction, val = d.split("=")
        if direction[-1] == "x":
            xsize = int(val) * 2 + 1 if xsize == 0 else xsize
            fold_dirs.append("left")
        else:
            ysize = int(val) * 2 + 1 if ysize == 0 else ysize
            fold_dirs.append("up")
    
    starting_paper = np.zeros((ysize, xsize), dtype = bool)
    for d in dot_data.split("\n"):
        c = d.split(",")
        starting_paper[int(c[1]), int(c[0])] = True

# Looking at the inputs, it is apparent that each time the
# paper is folded, it is folded in half. So we only need to
# know whether the paper is folded horizontally or vertically.
def fold(paper, direction):
    rows, cols = paper.shape
    if direction == "up":
        folded_paper = paper[:rows//2] + np.flipud(paper[(rows + 1)//2:])
    else:
        folded_paper = paper[:,:cols//2] \
            + np.fliplr(paper[:,(cols + 1)//2:])
    return folded_paper

# PART ONE
res1 = np.sum(fold(starting_paper, fold_dirs[0]))
print(f"Part 1: The number of visible dots after the first fold is {res1}.")

# PART TWO
paper = starting_paper.copy()
for d in fold_dirs:
    paper = fold(paper, d)

res2 = "\n".join("".join("#" if x else " " for x in l) for l in paper)
print(f"Part 2: The code is \n{res2}")

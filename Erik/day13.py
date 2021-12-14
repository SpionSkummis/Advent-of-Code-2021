import numpy as np

with open("Erik/inputs/input13.txt", "r") as f:
    all_file = f.read()
    f1, f2 = all_file.split("\n\n")
    dots = [(int(x.split(",")[0]),int(x.split(",")[1])) for x in f1.split("\n")]
    folds = [((x.split("=")[0].strip("fold along ")),int(x.split("=")[1])) for x in f2.strip().split("\n")]

xmax = max([x[0] for x in dots])
ymax = max([x[1] for x in dots])

paper = np.zeros((ymax+1, xmax+1))
for dot in dots:
    paper[dot[1]][dot[0]] = 1

def fold(old_paper, folding_instruction):
    axis = folding_instruction[0]
    value = folding_instruction[1]

    if axis == "y":
        upper = old_paper[0:value]
        lower = old_paper[value+1:]
        new_lower = lower[::-1]
#        len_diff = len(upper) - len(new_lower)
#        if len_diff < 0:
#            new_lower = np.pad(new_lower)
        new_paper = upper + new_lower
        return new_paper
    else:
        left = old_paper[:,0:value]
        right = old_paper[:,value+1:]
        new_right = right[::,::-1]
        new_paper = left + new_right
        return new_paper
        

# Part 1
part1 = fold(paper, folds[0])

dot_count = 0
for x in range(len(part1)):
    for y in range(len(part1[0])):
        if part1[x][y] > 0:
            dot_count += 1
print(f"Part 1 - Dots visible after first fold: {dot_count}")

final_paper = paper.copy()
for instr in folds:
    final_paper = fold(final_paper, instr)

prettyprint = ""
for row in final_paper:
    for num in row:
        if num > 0:
            prettyprint += "#"
        else:
            prettyprint += " "
    prettyprint += "\n"

print("Part 2 - Congratulations! Your activation code is: ")
print(prettyprint)

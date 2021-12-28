import numpy as np
# ()[]{}<>
with open("Erik/inputs/input10.txt", "r") as f:
    lines = [x.strip() for x in f]

def quickcheck(in_line):
    templist = []
    for char in in_line:
        if char in "[{(<":
            templist.append(char)
        else:
            if char == "]":
                if templist[-1] == "[":
                    templist.pop()
                else:
                    return 57
            elif char == "}":
                if templist[-1] == "{":
                    templist.pop()
                else:
                    return 1197
            elif char == ")":
                if templist[-1] == "(":
                    templist.pop()
                else:
                    return 3
            elif char == ">":
                if templist[-1] == "<":
                    templist.pop()
                else:
                    return 25137
    return 0

def linefinish(in_line):
    templist = []
    for char in in_line:
        if char in "[{(<":
            templist.append(char)
        else:
            templist.pop()
    
    finish_score = 0
    for char in reversed(templist):
        finish_score *= 5
        if char == "[":
            finish_score += 2
        elif char == "{":
            finish_score += 3
        elif char == "(":
            finish_score += 1
        elif char == "<":
            finish_score += 4

    return finish_score

#Part 1:
lines2 = [] #Needed for part 2
syn_err_score = 0
for line in lines:
    tempscore = quickcheck(line)
    if tempscore == 0:
        lines2.append(line) #Needed for part 2
    syn_err_score += tempscore

print(f"The syntax error score is: {syn_err_score}")

#Part 2:

all_autocomplete_scores = []
for line in lines2:
    all_autocomplete_scores.append(linefinish(line))
autocomplete_score = int(np.median(all_autocomplete_scores))
print(f"The autocomplete score is: {autocomplete_score}")

import numpy as np

# COMMON FUNCTIONS


def check_for_bingo(board):
    return not all(np.sum(~board["checked"], axis=0)) \
           or not all(np.sum(~board["checked"], axis=1))


def create_board(raw_data):
    bingo_numbers = np.array([[int(x) for x in l.split()] for l in raw_data])
    board = {"bingo": False,
             "checked": np.zeros((5,5), dtype="bool"),
             "numbers": bingo_numbers}
    return board

# PARSING INPUT


with open("inputs/day04.txt") as f:
    numbers = [int(d) for d in f.readline().split(",")]
    raw_boards = [line.strip() for line in f.readlines() if line.strip()]
    boards = []
    for i in range(len(raw_boards) // 5):
        boards.append(create_board(raw_boards[5*i:5*(i+1)]))

# PART 1 AND 2
bingo_order = []
for i in range(len(numbers)):
    j = 0
    for b in boards:
        if not b["bingo"]:
            match = np.where(b["numbers"] == numbers[i])
            if len(match[0]) > 0:
                b["checked"][match[0][0], match[1][0]] = True
                if check_for_bingo(b):
                    b["bingo"] = True
                    bingo_order.append((numbers[i], j))
        j += 1

res1 = np.sum(np.multiply(~boards[bingo_order[0][1]]["checked"],
                          boards[bingo_order[0][1]]["numbers"])) \
       * bingo_order[0][0]
res2 = np.sum(np.multiply(~boards[bingo_order[-1][1]]["checked"],
                          boards[bingo_order[-1][1]]["numbers"])) \
       * bingo_order[-1][0]

print(f"Part 1: The final score of the first bingo board is {res1}")
print(f"Part 2: The final score of the last bingo board is {res2}")

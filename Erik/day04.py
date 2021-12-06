import numpy as np

with open("Erik/inputs/input04.txt", "r") as f:
    numbers = [int(x) for x in f.readline().strip().split(",")]
    raw_boards = f.read().strip().split("\n\n")
    raw_boards = [x.split("\n") for x in raw_boards]
    boards = []
    for raw_board in raw_boards:
        temp_board = [[int(x) for x in y.split()] for y in raw_board]
        boards.append(np.array(temp_board))

board_markings = [np.zeros((5,5)) for x in range(len(boards))]


winner_id = -1
last_called = -1

for num in numbers:
    for a in range(len(boards)):
        for x in range(5):
            for y in range(5):
                if boards[a][x][y] == num:
                    board_markings[a][x][y] = 1
    
    for a in range(len(boards)):
        if 5 in np.sum(board_markings[a],(0)):
            winner_id = a
            last_called = num
            break
        if 5 in np.sum(board_markings[a],(1)):
            winner_id = a
            last_called = num
            break
    if winner_id > -1:
        break

winner_score = 0
for x in range(5):
    for y in range(5):
        if board_markings[winner_id][x][y] == 0:
            winner_score += boards[winner_id][x][y]

print(f"{last_called}!\nBINGO!!!\nFirst winning score is: {winner_score*last_called}\n")

""" PART 2 """
board_markings2 = [np.zeros((5,5)) for x in range(len(boards))]
winner_ids = []
last_calleds = []

for num in numbers:
    for a in range(len(boards)):
        if a in winner_ids:
            pass
        else:
            for x in range(5):
                for y in range(5):
                    if boards[a][x][y] == num:
                        board_markings2[a][x][y] = 1
        if a in winner_ids:
            pass
        else:
            if 5 in np.sum(board_markings2[a],(0)):
                winner_ids.append(a)
                last_calleds.append(num)
            if 5 in np.sum(board_markings2[a],(1)):
                winner_ids.append(a)
                last_calleds.append(num)

winner_score = 0
for x in range(5):
    for y in range(5):
        if board_markings2[winner_ids[-1]][x][y] == 0:
            winner_score += boards[winner_ids[-1]][x][y]

print(f"...{last_calleds[-1]}?\nbingo...\nLast winning score is: {winner_score*last_calleds[-1]}")

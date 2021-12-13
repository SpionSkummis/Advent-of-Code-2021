import numpy as np
print('Advent of Code 2021 - December 04 - Olof')

input = open('Olof\day04_input.txt','r').read().splitlines()
numbers = [int(a) for a in list(input[0].split(','))]
board, boards = [], []
for i in range(1, len(input)):
    if len(input[i].strip().split()) == 5:
        board.append(input[i].strip().split())
    if len(board) == 5:
        boards.append(np.array(board).astype(int))
        board = []

def hasBingo(board:np.ndarray):
    for i in range(5):
        if np.count_nonzero(board[i, 0:5] < 0) == 5 or np.count_nonzero(board[0:5, i] < 0) == 5:
            return True
    return False

part1, part2 = 0, 0
while part1 == 0 or part2 == 0: 
    drawn = numbers.pop(0)
    nonBingoBoards = []
    for board in boards:
        board[board == drawn] = -1
        if hasBingo(board):
            if part1 == 0:
                print('Part 1: ' + str(drawn * np.sum(board[board>0])))
                part1 = 1
            if len(boards) == 1: # sista brickan kvar
                print('Part 2: ' + str(drawn * np.sum(board[board>0])))
                part2 = 1
        else:
            nonBingoBoards.append(board) # nonBingoBoards går vidare till nästa runda
    boards = nonBingoBoards
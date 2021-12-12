import numpy as np
# 27594 is too high

print('Advent of Code 2021 - December 04 - Olof')
input = open('Olof\day04_input.txt','r').read().splitlines()
#--------------------------------------------------------------------------
# Nummer som ska dras hamnar i numbers
numbers = [int(a) for a in list(input[0].split(','))]
print(numbers)
#--------------------------------------------------------------------------
# Spelbrickor hamnar i boards. 100 st. Har försökt kontrollera att alla även är 5x5 osv. Tycker det ser rätt ut
boards = []
board = []
for i in range(1, len(input)):
    if len(input[i].strip().split()) == 5:
        board.append(input[i].strip().split())
    if len(board) == 5:
        boards.append(np.array(board).astype(int))
        board = []
#--------------------------------------------------------------------------
# Funktion som kontrollerar om en bricka har bingo.
# Givet en rad eller kolumn, count de som är -1 (<0). Om vi hittar 5 st -1 så har vi bingo. 
def hasBingo(board:np.ndarray):
    for i in range(5):
        if np.count_nonzero(board[i, 0:5] < 0) == 5: #kolla rad-bingo
            return True
        if np.count_nonzero(board[0:5, i] < 0) == 5: #kolla kolumn-bingo
            return True
    return False
#--------------------------------------------------------------------------
# Bingo-loopen:
# Loopa så länge det finns nummer kvar att dra
while len(numbers) > 0:
    nbr = numbers.pop(0)
    print('Drawing number: ' + str(nbr))
  
    # Gå igenom alla boards och sätt -1 på alla ställen som den dragna siffran står
    for board in boards:
        board[board == nbr] = -1

    if hasBingo(board): #hasBingo egen funktion
        print('BINGO')        
        print(board)
        print('Score: ' + str(nbr * np.sum(board[board>0])))
#--------------------------------------------------------------------------
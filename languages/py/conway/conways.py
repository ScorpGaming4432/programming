#newboard = [[0]*10]*10
newboard = open('conwayboard.txt').readlines()
for i in range(len(newboard)):
    newboard[i] = newboard[i].split()
    newboard[i] = list(map(int, [*newboard[i][0]]))
'''newboard = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]'''

'''def sum_in_radius(row, col):
    # Initialize the sum to 0
    total_sum = -board[row][col]
    # Get the number of rows and columns in the matrix
    cols = len(board[0])
    
    # Loop through the elements in the 3x3 grid centered on (row, col)
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            # Check if the current indices are within the bounds of the matrix
            if 0 <= i < board_length and 0 <= j < cols:
                total_sum += board[i][j]
    
    return total_sum'''


board_length = len(newboard)
def lifecheck(i, j):
    if i and board_length - 1 - i: #unreadable i != 0 and i != len(board) - 1
        checks = board[i+1][j] + board[i-1][j]
        if not j:
            return checks + board[i][j+1] + board[i+1][j+1] + board[i-1][j+1]
        elif not len(board[i]) - 1 - j:
            return checks + board[i][j-1] + board[i+1][j-1] + board[i-1][j-1]
        else:
            return checks + board[i][j+1] + board[i+1][j+1] + board[i-1][j+1] + board[i][j-1] + board[i+1][j-1] + board[i-1][j-1]
    elif not i:
        checks = board[i+1][j]
        if not j:
            return checks + board[i][j+1] + board[i+1][j+1]
        elif not len(board[i]) - 1 - j:
            return checks + board[i][j-1] + board[i+1][j-1]
        else:
            return checks + board[i][j+1] + board[i+1][j+1] + board[i][j-1] + board[i+1][j-1]
    else:
        checks = board[i-1][j]
        if not j:
            return checks + board[i][j+1] + board[i-1][j+1]
        elif not len(board[i]) - 1 - j:
            return checks + board[i][j-1] + board[i-1][j-1]
        else:
            return checks + board[i][j+1] + board[i-1][j+1] + board[i][j-1] + board[i-1][j-1]



board = []
steps = 0
frameratelimit = 0
from time import time, sleep
starttime = time()
while newboard != board:
    t0 = time()

    board = newboard
    newboard = []
    steps += 1
    print(steps)

    for i in range(len(board)):
        podnewboard = []
        for j in range(len(board[i])):
            curchk = lifecheck(i, j)
            if not curchk - 3:
                podnewboard.append(1)
            elif not curchk - 2:
                podnewboard.append(board[i][j])
            else:
                podnewboard.append(0)
        newboard.append(podnewboard)

    printout = str(steps) + '\n'
    for pod in board:
        line = "".join(str(num) for num in pod)
        #print(line)
        printout += line.replace("0", "⬜").replace("1", "⬛") + "\n"
    print(printout)

    if frameratelimit > 0 :sleep((1/frameratelimit)-(t0-time())) #deltaTime (but mine)
else:
    print('end. \nsteps:', steps, f'\ntime taken to break: {time() - starttime}s')
print(len(board))
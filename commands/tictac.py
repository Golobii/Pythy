import numpy as np

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


a = np.array(board)
for row in board:
    for number in row:
        if number == 5:
            b = np.where(a==number)
            x = b[0][0]
            y = b[1][0]
            board[x][y] = "X"

for row in board:
    print(row)


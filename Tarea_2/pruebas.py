board = [[0 for _ in range(4)] for _ in range(4)]
N = len(board)
for row in range(N):
    for col in range(N):
        if board[row][col] != 1:
            board[row][col] = 1
            

print(board)



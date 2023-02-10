import sys
input = sys.stdin.readline

def func1(board, best):
    row = 0
    for i in board:
        val = None
        count = 1
        col = 0
        for j in i:
            if val:
                if j == val:
                    count += 1
                else:
                    val = j
                    if best <= count:
                        best = count
                    count = 1
            else:
                val = j
            col += 1
        if best < count:
            best = count
        row += 1
    return best


N = int(input())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))
board_T = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
for i in range(len(board)):
    for j in range(len(board[0])):
        board_T[i][j] = board[j][i]

best = 0

# best = func1(board, best)
# best = func1(board_T, best)
for i in range(len(board)):
    for j in range(len(board[i])):
        if i != 0 and board[i][j] != board[i-1][j]:
            board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
            best = func1(board, best)
            board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
        if i != len(board)-1 and board[i][j] != board[i+1][j]:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            best = func1(board, best)
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
        if j != 0 and board[i][j] != board[i][j - 1]:
            board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
            best = func1(board, best)
            board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
        if j != len(board[0]) - 1 and board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            best = func1(board, best)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

for i in range(len(board_T)):
    for j in range(len(board_T[i])):
        if i != 0:
            board_T[i][j], board_T[i - 1][j] = board_T[i - 1][j], board_T[i][j]
            best = func1(board_T, best)
            board_T[i][j], board_T[i - 1][j] = board_T[i - 1][j], board_T[i][j]
        if i != len(board_T)-1:
            board_T[i][j], board_T[i + 1][j] = board_T[i + 1][j], board_T[i][j]
            best = func1(board_T, best)
            board_T[i][j], board_T[i + 1][j] = board_T[i + 1][j], board_T[i][j]


print(best)
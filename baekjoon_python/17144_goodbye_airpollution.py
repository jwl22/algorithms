import copy
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

R, C, T = map(int, input().rstrip().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().rstrip().split())))
board_copy = copy.deepcopy(board)


def diffuse(y, x):
    global R, C

    for i in range(4):
        if x + dx[i] < C and x + dx[i] >= 0 and y + dy[i] < R and y + dy[i] >= 0 and board_copy[y + dy[i]][
            x + dx[i]] != -1:
            board_copy[y + dy[i]][x + dx[i]] += board[y][x] // 5
            board_copy[y][x] -= board[y][x] // 5


def cycle(pos):
    global R, C

    tmp = copy.deepcopy(board_copy)
    for i in range(C):
        if i == C - 1:
            board_copy[0][i] = tmp[1][i]
            board_copy[R - 1][i] = tmp[R - 2][i]
            board_copy[pos][i] = tmp[pos][i - 1]
            board_copy[pos + 1][i] = tmp[pos + 1][i - 1]
        else:
            board_copy[0][i] = tmp[0][i + 1]
            board_copy[R - 1][i] = tmp[R - 1][i + 1]
            if i == 1:
                board_copy[pos][i] = 0
                board_copy[pos + 1][i] = 0
            elif i > 1:
                board_copy[pos][i] = tmp[pos][i - 1]
                board_copy[pos + 1][i] = tmp[pos + 1][i - 1]
    for i in range(1, R - 1):
        if i < pos:
            board_copy[i][0] = tmp[i - 1][0]
            board_copy[i][C - 1] = tmp[i + 1][C - 1]
        elif i > pos + 1:
            board_copy[i][0] = tmp[i + 1][0]
            board_copy[i][C - 1] = tmp[i - 1][C - 1]


cleaner = False
for t in range(T):
    for i in range(R):
        for j in range(C):
            if board_copy[i][j] == -1 and not cleaner:
                cleaner = i
            if board_copy[i][j] != 0 and board_copy[i][j] != -1:
                diffuse(i, j)
    cycle(cleaner)
    board = copy.deepcopy(board_copy)

result = 0
for i in board_copy:
    result += sum(i)
result += 2  # -1로 채워진 두 칸(공기청정기) 값 더하기 위해 +2
print(result)

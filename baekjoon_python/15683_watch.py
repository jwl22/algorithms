import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

best = N*M


def one(i, j, d, board_copy):
    global N, M

    if 0 in d:
        for c in range(i, -1, -1):
            if board_copy[c][j] == 6:
                break
            elif board_copy[c][j] == 0:
                board_copy[c][j] = -1
    if 1 in d:
        for c in range(i, N):
            if board_copy[c][j] == 6:
                break
            elif board_copy[c][j] == 0:
                board_copy[c][j] = -1
    if 2 in d:
        for r in range(j, -1, -1):
            if board_copy[i][r] == 6:
                break
            elif board_copy[i][r] == 0:
                board_copy[i][r] = -1
    if 3 in d:
        for r in range(j, M):
            if board_copy[i][r] == 6:
                break
            elif board_copy[i][r] == 0:
                board_copy[i][r] = -1
    scan(i, j, board_copy)


def scan(c, r, board2):
    global N, M

    global best
    for j in range(r+1, M):
        if board2[c][j] == 1:
            for k in range(4):
                one(c, j, [k], copy.deepcopy(board2))
        elif board2[c][j] == 2:
            one(c, j, [0, 1], copy.deepcopy(board2))
            one(c, j, [2, 3], copy.deepcopy(board2))
        elif board2[c][j] == 3:
            one(c, j, [0, 3], copy.deepcopy(board2))
            one(c, j, [3, 1], copy.deepcopy(board2))
            one(c, j, [1, 2], copy.deepcopy(board2))
            one(c, j, [2, 0], copy.deepcopy(board2))
        elif board2[c][j] == 4:
            one(c, j, [2, 0, 3], copy.deepcopy(board2))
            one(c, j, [0, 3, 1], copy.deepcopy(board2))
            one(c, j, [3, 1, 2], copy.deepcopy(board2))
            one(c, j, [1, 2, 0], copy.deepcopy(board2))
        elif board2[c][j] == 5:
            one(c, j, [0, 1, 2, 3], copy.deepcopy(board2))
    for i in range(c+1, N):
        for j in range(0, M):
            if board2[i][j] == 1:
                for k in range(4):
                    one(i, j, [k], copy.deepcopy(board2))
            elif board2[i][j] == 2:
                one(i, j, [0, 1], copy.deepcopy(board2))
                one(i, j, [2, 3], copy.deepcopy(board2))
            elif board2[i][j] == 3:
                one(i, j, [0, 3], copy.deepcopy(board2))
                one(i, j, [3, 1], copy.deepcopy(board2))
                one(i, j, [1, 2], copy.deepcopy(board2))
                one(i, j, [2, 0], copy.deepcopy(board2))
            elif board2[i][j] == 4:
                one(i, j, [2, 0, 3], copy.deepcopy(board2))
                one(i, j, [0, 3, 1], copy.deepcopy(board2))
                one(i, j, [3, 1, 2], copy.deepcopy(board2))
                one(i, j, [1, 2, 0], copy.deepcopy(board2))
            elif board2[i][j] == 5:
                one(i, j, [0, 1, 2, 3], copy.deepcopy(board2))
    zeros = 0
    for i in board2:
        for j in i:
            if j == 0:
                zeros += 1
    best = min(best, zeros)


scan(0, -1, board)
print(best)

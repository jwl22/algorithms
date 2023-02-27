import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = []
for i in range(N):
    board.append(list(input().rstrip()))

result = M * N
for i in range(N - 7):
    for j in range(M - 7):

        count_B, count_W = 0, 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0:
                        if board[i + k][j + l] == 'W':
                            count_B += 1
                        else:
                            count_W += 1
                    else:
                        if board[i + k][j + l] == 'W':
                            count_W += 1
                        else:
                            count_B += 1
                else:
                    if l % 2 == 0:
                        if board[i + k][j + l] == 'W':
                            count_W += 1
                        else:
                            count_B += 1
                    else:
                        if board[i + k][j + l] == 'W':
                            count_B += 1
                        else:
                            count_W += 1
        result = min(result, count_W, count_B)

print(result)

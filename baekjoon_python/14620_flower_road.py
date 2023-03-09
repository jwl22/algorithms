import sys
from itertools import combinations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

value = [[1000 for _ in range(N)] for _ in range(N)]


def scan(y, x):
    value[y][x] = board[y][x]
    for i in range(4):
        value[y][x] += board[y + dy[i]][x + dx[i]]


for i in range(1, N - 1):
    for j in range(1, N - 1):
        scan(i, j)
rc = [(r, c) for r in range(1, N - 1) for c in range(1, N - 1)]
cand = list(combinations(rc, 3))
best = 3000
for i in cand:
    visited = []

    flag = 0
    tmp = 0
    for j in range(3):
        tmp += value[i[j][0]][i[j][1]]
        if i[j] not in visited:
            visited.append((i[j]))
        else:
            flag = 1
        for k in range(4):
            if (i[j][0] + dx[k], i[j][1] + dy[k]) not in visited:
                visited.append((i[j][0] + dx[k], i[j][1] + dy[k]))
            else:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0 and j == 2:
        best = min(best, tmp)

print(best)

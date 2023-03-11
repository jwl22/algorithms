import sys
from collections import deque

sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

field = []
for i in range(N):
    field.append(list(map(int, input().rstrip())))

cost = [[[M * N, M * N] for _ in range(M)] for _ in range(N)]
cost[0][0] = [1, 1]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()
q.append([0, 0, 0, -1])

while q:
    tmp = q.popleft()
    y, x, is_break, d = tmp[0], tmp[1], tmp[2], tmp[3]

    for i in range(4):
        if d == 0 and i == 1 or d == 1 and i == 0 or d == 2 and i == 3 or d == 3 and i == 2:
            continue
        if y + dy[i] < N and y + dy[i] >= 0 and x + dx[i] < M and x + dx[i] >= 0:
            if is_break == 0:
                if field[y + dy[i]][x + dx[i]] == 1:
                    if cost[y + dy[i]][x + dx[i]][1] > cost[y][x][0] + 1:
                        cost[y + dy[i]][x + dx[i]][1] = cost[y][x][0] + 1
                        q.append([y + dy[i], x + dx[i], 1, i])
                    else:
                        continue
                else:
                    if cost[y + dy[i]][x + dx[i]][0] > cost[y][x][0] + 1:
                        cost[y + dy[i]][x + dx[i]][0] = cost[y][x][0] + 1
                        q.append([y + dy[i], x + dx[i], 0, i])
                    else:
                        continue
            else:
                if field[y + dy[i]][x + dx[i]] == 1:
                    continue
                else:
                    if cost[y + dy[i]][x + dx[i]][1] > cost[y][x][1] + 1:
                        cost[y + dy[i]][x + dx[i]][1] = cost[y][x][1] + 1
                        q.append([y + dy[i], x + dx[i], 1, i])
                    else:
                        continue

if min(cost[N - 1][M - 1]) == M * N and (M != 1 and N != 1):
    print(-1)
else:
    print(min(cost[N - 1][M - 1]))

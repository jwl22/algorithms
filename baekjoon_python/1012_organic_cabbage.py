import sys

sys.setrecursionlimit(20000)

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0


def chk(i, j):
    global M, N

    if board[i][j] == 0:
        return False
    board[i][j] = 0
    for k in range(4):
        if j + dx[k] >= 0 and i + dy[k] >= 0 and j + dx[k] < M and i + dy[k] < N and board[i + dy[k]][j + dx[k]] == 1:
            chk(i + dy[k], j + dx[k])
    return True


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().rstrip().split())  # 가로 세로 배추개수
    board = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().rstrip().split())
        board[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if chk(i, j):
                count += 1

    print(count)
    count = 0

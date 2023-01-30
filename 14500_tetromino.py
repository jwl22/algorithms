import sys
input = sys.stdin.readline

ans = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N, M = map(int, input().rstrip().split())
board = []
for i in range(N):
    board.append(input().rstrip().split())
board = [[int(x) for x in i] for i in board]
visited = [[0 for _ in range(M)] for _ in range(N)]

def search(y, x, sum, cnt):
    if cnt == 4:
        global ans
        ans = max(ans, sum)
        return
    if x<0 or x>=M or y<0 or y>=N:
        return
    if visited[y][x]:
        return

    visited[y][x] = 1
    for i in range(4):
        search(y+dy[i], x+dx[i], sum+board[y][x], cnt+1)
    visited[y][x] = 0

for i in range(N):
    for j in range(M):
        search(i,j,0,0)

        if j+2 < M:
            if i+1 < N:
                ans = max(ans, board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1])
            if i-1 >= 0:
                ans = max(ans, board[i][j] + board[i][j+1] + board[i][j+2] + board[i-1][j+1])
        if i+2 < N:
            if j+1 < M:
                ans = max(ans, board[i][j] + board[i+1][j] + board[i+1][j + 1] + board[i + 2][j])
            if j-1 >= 0:
                ans = max(ans, board[i][j] + board[i+1][j] + board[i+1][j - 1] + board[i + 2][j])

print(ans)
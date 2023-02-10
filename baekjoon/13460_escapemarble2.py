import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().rstrip().split())

result = 11

board = []
for _ in range(N):
    board.append(input().rstrip())

R, B = [], []
for i in range(N):
    if 'R' in board[i]:
        R = [i, board[i].index('R')]
    if 'B' in board[i]:
        B = [i, board[i].index('B')]
def chk(r, b, d, count):
    if count > 10 or (board[r[0]+dy[d]][r[1]+dx[d]] == '#' and board[b[0]+dy[d]][b[1]+dx[d]] == '#'):
        return
    global result
    r_b = r.copy()
    b_b = b.copy()

    flag = 0
    while board[r[0]+dy[d]][r[1]+dx[d]] != '#':
        if board[r[0]+dy[d]][r[1]+dx[d]] == 'O':
            flag = 1
        r[0] += dy[d]
        r[1] += dx[d]
    while board[b[0]+dy[d]][b[1]+dx[d]] != '#':
        if board[b[0]+dy[d]][b[1]+dx[d]] == 'O':
            return
        b[0] += dy[d]
        b[1] += dx[d]
    if flag == 1:
        if count < result:
            result = count
        return

    if r == b:
        if d == 0:
            if r_b[0] < b_b[0]:
                b[0] += 1
            else:
                r[0] += 1
        elif d == 1:
            if r_b[0] < b_b[0]:
                r[0] -= 1
            else:
                b[0] -= 1
        elif d == 2:
            if r_b[1] < b_b[1]:
                b[1] += 1
            else:
                r[1] += 1
        elif d == 3:
            if r_b[1] < b_b[1]:
                r[1] -= 1
            else:
                b[1] -= 1

    if d == 0:
        scan(r, b, count, 1)
    elif d == 1:
        scan(r, b, count, 0)
    elif d == 2:
        scan(r, b, count, 3)
    elif d == 3:
        scan(r, b, count, 2)

def scan(r, b, count, prev):
    for i in range(4):
        if i == prev:
            continue
        chk(r.copy(), b.copy(), i, count + 1)

scan(R, B, 0, -1)

if result > 10:
    print(-1)
else:
    print(result)
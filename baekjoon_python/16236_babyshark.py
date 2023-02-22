import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
s_p = []
field = []
for i in range(N):
    tmp = list(map(int, input().rstrip().split()))
    if 9 in tmp:
        s_p = [i, tmp.index(9)]
    field.append(tmp)
field[s_p[0]][s_p[1]] = 0


def scan(size, pos):
    global N

    q_list = deque()
    p_list = []
    visited = [pos]
    for i in range(4):
        x = pos[1]+dx[i]
        y = pos[0]+dy[i]
        if x >= 0 and x < N and y >= 0 and y < N:
            if field[y][x] == size or field[y][x] == 0:
                q_list.append([y, x, 1])
            elif field[y][x] < size:
                if not p_list:
                    p_list = [y, x, 1]
                elif (p_list[0] > y) or (p_list[0] == y and p_list[1] > x):
                    p_list = [y, x, 1]
    if not p_list:
        while q_list:
            q = q_list.popleft()
            if [q[0], q[1]] in visited:
                continue
            visited.append([q[0], q[1]])
            if p_list and q[2]+1 != p_list[2]:
                break
            for i in range(4):
                x = q[1]+dx[i]
                y = q[0]+dy[i]
                if x >= 0 and x < N and y >= 0 and y < N:
                    if field[y][x] == size or field[y][x] == 0:
                        q_list.append([y, x, q[2]+1])
                    elif field[y][x] < size:
                        if not p_list:
                            p_list = [y, x, q[2]+1]
                        elif (p_list[0] > y) or (p_list[0] == y and p_list[1] > x):
                            p_list = [y, x, q[2]+1]
                        # if [y, x, q[2]+1] not in p_list:
                        #     p_list.append([y, x, q[2]+1])

    if p_list:
        # p_list = sorted(p_list, key=lambda x: (x[0], x[1]))
        return p_list
    else:
        return False


size = deque([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6])

cost = 0
while size:
    i = size.popleft()
    result = scan(i, s_p)
    if not result:
        break
    cost += result[2]
    field[result[0]][result[1]] = 0
    s_p = [result[0], result[1]]
if not size:
    while True:
        result = scan(7, s_p)
        if not result:
            break
        cost += result[2]
        field[result[0]][result[1]] = 0
        s_p = [result[0], result[1]]

print(cost)

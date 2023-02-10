import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
line = deque(input().rstrip())

line_split = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        line_split[i][j] = line.popleft()

ans = deque()


def chk(val):
    for i in range(val + 1):
        s = 0
        for j in range(i, -1, -1):
            s += ans[j]
            if line_split[j][i] == '+' and s <= 0:
                return False
            elif line_split[j][i] == '-' and s >= 0:
                return False
            elif line_split[j][i] == '0' and s != 0:
                return False
    return True

def solve(val):
    if val == n:
        for i in ans:
            print(i, end=' ')
        exit()
    if line_split[val][val] == '+':
        for i in range(1, 11):
            ans.append(i)
            if chk(val):
                solve(val+1)
            ans.pop()
    elif line_split[val][val] == '-':
        for i in range(-10, 0):
            ans.append(i)
            if chk(val):
                solve(val+1)
            ans.pop()
    else:
        ans.append(0)
        if chk(val):
            solve(val + 1)
        ans.pop()
solve(0)

print()

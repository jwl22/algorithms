import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def D(A):
    A *= 2
    if A > 9999:
        A %= 10000
    return A


def S(A):
    if A == 0:
        A = 9999
    else:
        A -= 1
    return A


def L(A):
    f = A % 1000
    b = A // 1000
    return f*10 + b


def R(A):
    f = A % 10
    b = A // 10
    return f*1000 + b


for _ in range(T):
    A, B = map(int, input().rstrip().split())
    visited = [False] * 10000
    tmp = deque()
    tmp.append([A, ""])

    while True:
        now_a, path = tmp.popleft()
        if now_a == B:
            print(path)
            break

        a = D(now_a)
        if visited[a] == False:
            visited[a] = True
            tmp.append([a, path+'D'])

        a = S(now_a)
        if visited[a] == False:
            visited[a] = True
            tmp.append([a, path+'S'])

        a = L(now_a)
        if visited[a] == False:
            visited[a] = True
            tmp.append([a, path+'L'])

        a = R(now_a)
        if visited[a] == False:
            visited[a] = True
            tmp.append([a, path+'R'])

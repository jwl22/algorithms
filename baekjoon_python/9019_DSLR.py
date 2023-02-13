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
    A = str(A)
    if len(A) != 4:
        A += '0'
    else:
        A = A[1:] + A[0]
    A = int(A)
    return A


def R(A):
    A = str(A)
    while len(A) != 4:
        A = '0'+A
    A = A[-1] + A[:-1]
    A = int(A)
    return A


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

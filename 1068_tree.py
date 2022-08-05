from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))

child = deque()
for i in range(N):
    child.append([i])
child[1].append(1)
print(child)
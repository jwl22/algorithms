from collections import deque
from re import A
import sys
input = sys.stdin.readline

K = int(input())
visited = deque(map(int, input().split()))

level = deque()
for _ in range(K):
    level.append(deque())

depth = K
count = 2 ** (depth-1)
while visited:
    level[depth-1].append(visited.popleft())
    visited.rotate(-1)
    count -= 1
    if count <= 0:
        visited.rotate(1)
        depth -= 1
        count = 2 ** (depth-1)

for i in range(len(level)):
    for j in level[i]:
        print(j, end=' ')
    print()

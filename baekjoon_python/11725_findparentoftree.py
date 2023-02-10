from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

tree = dict()
for i in range(1, N+1):
    tree[i] = []
for _ in range(N-1):
    d1, d2 = map(int, input().split())
    tree[d1].append(d2)
    tree[d2].append(d1)

queue = deque()
parent = dict()

for i in range(1, N+1):
    for j in tree[i]:
        parent[j] = ''

queue.append(1)
while queue:
    i = queue.popleft()
    for j in tree[i]:
        if j == parent[i]:
            continue
        parent[j] = i

    for j in tree[i]:
        if j == parent[i]:
            continue
        queue.append(j)

parent_sorted = sorted(parent.items())
for i in parent_sorted:
    if i[0] == 1:
        continue
    print(i[1])

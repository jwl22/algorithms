import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

best = 0
tmp = [deque() for _ in range(100000)]
tmp_idx = 0
count = 0
for i in range(len(A)):
    count += 1
    tmp[A[i]-1].append(i)
    if len(tmp[A[i]-1]) > K:
        pop_idx = tmp[A[i]-1].popleft()
        if pop_idx < tmp_idx:
            continue
        else:
            best = max(best, i-tmp_idx)
            tmp_idx = pop_idx + 1
best = max(best, count-tmp_idx)

print(best)

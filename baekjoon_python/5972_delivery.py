import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
way = dict()
for _ in range(1, M+1):
    A, B, C = map(int, input().rstrip().split())
    way.setdefault(A, []).append([B, C])
    way.setdefault(B, []).append([A, C])

loc_best = [1000*N]*N


def scan(loc):
    q = deque()
    q.append([loc, 0])
    loc_best[loc-1] = 0
    while q:
        n, c = q.popleft()
        if loc_best[n-1] < c:
            continue
        for i in way[n]:
            if c+i[1] < loc_best[i[0]-1]:
                q.append([i[0], c+i[1]])
                loc_best[i[0]-1] = c+i[1]


scan(1)

print(loc_best[N-1])

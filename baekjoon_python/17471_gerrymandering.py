import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().rstrip().split()))
area_info = [list(map(int, input().rstrip().split())) for _ in range(N)]

area_connected = dict()
for i in range(1, N+1):
    area_connected[i] = []
for i in range(N):
    for j in range(1, len(area_info[i])):
        area_connected[i+1].append(area_info[i][j])

visited = set()
count = 0
best = N*100


def dfs(i, l):
    global count, visited
    if i in visited or i not in l:
        return
    visited.add(i)
    count += people[i-1]
    for j in area_connected[i]:
        dfs(j, l)


def is_connected(l):
    global count, visited
    visited = set()
    count = 0
    dfs(l[0], l)
    if len(visited) != len(l):
        return False
    return True


Ns = {j+1 for j in range(N)}
dfs(1, Ns)
if len(visited) != N:
    not_visited = []
    for i in range(1, N+1):
        if i not in visited:
            not_visited.append(i)
    visited = set()
    count = 0
    dfs(not_visited[0], Ns)
    if len(visited) == len(not_visited):
        print(abs(count - (sum(people) - count)))
    else:
        print(-1)
else:
    for i in range(1, N//2+1):
        comb = list(combinations(Ns, i))
        for j in comb:
            k = list(Ns.difference(j))
            chk1 = is_connected(j)
            chk1_count = count
            chk2 = is_connected(k)
            chk2_count = count
            if chk1 and chk2:
                best = min(best, abs(chk1_count-chk2_count))
    print(best)

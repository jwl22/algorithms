import sys

input = sys.stdin.readline

N = int(input())
Ns = []
for _ in range(N):
    Ns.append(list(map(int, input().rstrip().split())))
Ns_end = sorted(Ns, key=lambda x: (x[1], x[0]))

e = 0
count = 0
for i in Ns_end:
    if i[0] >= e:
        count += 1
        e = i[1]

print(count)

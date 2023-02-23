import sys

input = sys.stdin.readline

N = int(input())
coord = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    coord.append([x, y])

coord = sorted(coord, key=lambda x: (x[0], x[1]))
for i in coord:
    print(i[0], i[1])

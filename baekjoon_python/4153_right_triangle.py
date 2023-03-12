import sys

input = sys.stdin.readline

while True:
    line = list(map(int, input().rstrip().split()))
    if line[0] == line[1] == line[2] == 0:
        break
    line.sort()
    if line[0] ** 2 + line[1] ** 2 == line[-1] ** 2:
        print("right")
    else:
        print("wrong")

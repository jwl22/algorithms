import sys

input = sys.stdin.readline

N = int(input())
Ns = list(map(int, input().rstrip().split()))
Ns.sort()
M = int(input())
Ms = list(map(int, input().rstrip().split()))


def find(n):
    global Ns

    min_n = 0
    max_n = len(Ns) - 1
    while True:
        if min_n > max_n:
            return 0
        if n > Ns[(min_n + max_n) // 2]:
            min_n = ((min_n + max_n) // 2) + 1
        elif n < Ns[(min_n + max_n) // 2]:
            max_n = ((min_n + max_n) // 2) - 1
        else:
            return 1


for i in Ms:
    print(find(i))

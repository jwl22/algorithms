import sys

input = sys.stdin.readline

N = int(input())
Ns = list(map(int, input().rstrip().split()))
M = int(input())
Ms = list(map(int, input().rstrip().split()))

N_dict = dict()
for i in Ns:
    if i in N_dict:
        N_dict[i] += 1
    else:
        N_dict[i] = 1

for i in Ms:
    if i in N_dict:
        print(N_dict[i], end=' ')
    else:
        print(0, end=' ')

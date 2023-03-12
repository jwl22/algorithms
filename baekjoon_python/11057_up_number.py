import sys

input = sys.stdin.readline

N = int(input())

Ns = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]]
for _ in range(N - 1):
    tmp = [Ns[-1][-1]]
    for i in range(9):
        tmp.append(tmp[-1] - Ns[-1][i])
    tmp.append(sum(tmp))
    Ns.append(tmp)

print(Ns[-1][-1] % 10007)

import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
if K == 0:
    print(1)
else:
    result = N
    for i in range(K - 1):
        result *= N - 1
        N -= 1

    for i in range(2, K + 1):
        result /= i

    print(int(result))

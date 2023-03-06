import sys

input = sys.stdin.readline

n = int(input())

result = 1
for i in range(n - 1):
    if i % 2 == 0:
        result = result * 2 + 1
    else:
        result = result * 2 - 1
print(result % 10007)

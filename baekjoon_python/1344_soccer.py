import sys
from itertools import combinations
input = sys.stdin.readline

A = int(input())
A /= 100
B = int(input())
B /= 100

result = 0

decimal = [2, 3, 5, 7, 11, 13, 17]
cases = []
for i in decimal:
    cases.append(len(list(combinations([i for i in range(1, 19)], i))))

for i in range(len(decimal)):
    result += A**decimal[i] * (1-A)**(18-decimal[i]) * cases[i]
    result += B**decimal[i] * (1-B)**(18-decimal[i]) * cases[i]

for i in range(len(decimal)):
    for j in range(len(decimal)):
        result -= A**decimal[i] * (1-A)**(18-decimal[i]) * B**decimal[j] * \
            (1-B)**(18-decimal[j]) * cases[i] * cases[j]

print(result)

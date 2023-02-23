import sys

input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
min_v = min(a, b)
max_v = max(a, b)
min_c = 1
for i in range(2, min_v + 1):
    if a % i == 0 and b % i == 0:
        min_c = i
print(min_c)

d = 1
while True:
    if (min_v * d) % max_v == 0:
        print(min_v * d)
        break
    d += 1

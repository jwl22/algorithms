import sys

input = sys.stdin.readline

N = int(input())
tips = []
for _ in range(N):
    tips.append(int(input()))
tips = sorted(tips, reverse=True)
sum = 0
for i in range(N):
    tmp = tips[i] - i
    if tmp > 0:
        sum += tmp
print(sum)

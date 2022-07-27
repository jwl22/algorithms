from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

cardstack = deque()

for i in range(N):
    cardstack.append(i+1)

while len(cardstack) != 1:
    cardstack.popleft()
    cardstack.rotate(-1)

print(cardstack[0])

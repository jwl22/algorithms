from collections import deque
import sys
input = sys.stdin.readline

queue_before = []
queue_after = deque()

N, K = map(int, input().split())

for i in range(N):
    queue_before.append(i+1)

index = K - 1
if len(queue_before) == 1:
    queue_after.append(queue_before.pop())
else:
    while queue_before:
        queue_after.append(queue_before.pop(index))
        index += K - 1
        if len(queue_before) == 1:
            queue_after.append(queue_before.pop())
        else:
            if index >= len(queue_before):
                index %= len(queue_before)

# 결과 출력
print("<", end="")
while queue_after:
    if len(queue_after) == 1:
        print(queue_after.pop(), end="")
        break
    print(queue_after.popleft(), end=", ")
print(">", end="")

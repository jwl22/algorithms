from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

stack = deque()
result = deque()
for i, v in enumerate(H):
    if i == 0:
        stack.append([i, v])
        result.append(0)
        continue
    stack_length = len(stack)
    for j in range(1, stack_length+1):
        if stack[stack_length-j][1] >= v:
            result.append(stack[stack_length-j][0]+1)
            if stack[stack_length-j][1] == v:
                stack.pop()
            break
        if stack[stack_length-j][1] <= v:
            stack.pop()
    if len(stack) == 0:
        result.append(0)
    stack.append([i, v])

for i in result:
    print(i, end=' ')

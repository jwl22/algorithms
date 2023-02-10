from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    command = input().split()
    if len(command) == 2:
        queue.append(command[1])
    elif command[0] == "pop":
        if queue:
            popitem = queue.popleft()
            print(popitem)
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)

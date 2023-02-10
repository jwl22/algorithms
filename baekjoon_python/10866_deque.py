from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
testdeque = deque()

for _ in range(N):
    command = input().split()
    if command[0] == "push_front":
        testdeque.appendleft(command[1])
    elif command[0] == "push_back":
        testdeque.append(command[1])
    elif command[0] == "pop_front":
        if testdeque:
            print(testdeque.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if testdeque:
            print(testdeque.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(testdeque))
    elif command[0] == "empty":
        if testdeque:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if testdeque:
            print(testdeque[0])
        else:
            print(-1)
    elif command[0] == "back":
        if testdeque:
            print(testdeque[len(testdeque)-1])
        else:
            print(-1)

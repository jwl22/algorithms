import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    command = input().split()
    if len(command) == 2:
        arr.append(int(command[1]))
    elif command[0] == "pop":
        if arr:
            popitem = arr.pop()
            print(popitem)
        else:
            print(-1)
    elif command[0] == "size":
        print(len(arr))
    elif command[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if arr:
            print(arr[len(arr)-1])
        else:
            print(-1)

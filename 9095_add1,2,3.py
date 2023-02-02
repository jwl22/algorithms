import sys
input = sys.stdin.readline

count = 0

def func1(n, num):
    global count
    if num == n:
        count += 1
        return
    if num > n:
        return
    for i in range(1,4):
        func1(n, num + i)
    return

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    count = 0
    func1(n, 0)
    print(count)
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
count = 1


def deleteone(A, B):
    global count
    prev_b = B
    while B % 10 != 1:
        if A < B and B % 2 == 0:
            B //= 2
            count += 1
        else:
            if prev_b == B:
                print(-1)
                exit()
            return B
    if B > 10:
        B //= 10
        count += 1
    return B


while A != B:
    B = deleteone(A, B)
    if A != B and B < A:
        print(-1)
        exit()
print(count)

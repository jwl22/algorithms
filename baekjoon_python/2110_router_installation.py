import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
X = []
for _ in range(N):
    x = int(input())
    X.append(x)
X.sort()
result = 1
visited = []


def chk(A, B):
    while A <= B:
        mid = (B+A)//2
        cur = X[0]
        count = 1
        for i in range(1, N):
            if X[i] - cur >= mid:
                count += 1
                cur = X[i]

        global C
        if count >= C:
            global result
            result = max(result, mid)
            A = mid+1
        else:
            B = mid-1


chk(1, X[-1])
print(result)

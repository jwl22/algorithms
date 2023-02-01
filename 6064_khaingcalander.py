import sys
import math
input = sys.stdin.readline

T = int(input())    # 테스트 수
for i in range(T):
    M, N, x, y = map(int, input().split())
    m, n = 0, 0
    while True:
        if M*m+x == N*n+y:
            result = M*m+x
            break
        if M*m+x < N*n+y:
            m += 1
        else:
            n += 1
        if M*m+x > math.lcm(M, N):
            result = -1
            break
    print(result)

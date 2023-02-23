import sys

input = sys.stdin.readline

while True:
    n, m = map(float, input().rstrip().split())
    n, m = int(n), int(m * 100)
    if n == 0:
        break
    cps = []
    for _ in range(int(n)):
        tmp = list(map(float, input().rstrip().split()))
        cps.append([int(tmp[0]), int(tmp[1] * 100 + 0.5)])

    # cps = sorted(cps, key=lambda x: -(x[0] / x[1]))

    dp = [0] * (m + 1)
    for i in range(1, m + 1):
        for j in cps:
            if i < j[1]:
                continue
            dp[i] = max(dp[i], dp[i - j[1]] + j[0])

    print(dp[m])

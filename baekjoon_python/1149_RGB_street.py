import sys

input = sys.stdin.readline

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().rstrip().split())))
dp = [cost[0].copy(), [1000] * 3]

for i in range(1, N):  # 0: R, 1:G, 2:B
    dp[1][0] = min(cost[i][0] + dp[0][1], cost[i][0] + dp[0][2])
    dp[1][1] = min(cost[i][1] + dp[0][0], cost[i][1] + dp[0][2])
    dp[1][2] = min(cost[i][2] + dp[0][0], cost[i][2] + dp[0][1])
    dp[0] = dp[1].copy()

print(min(dp[1]))

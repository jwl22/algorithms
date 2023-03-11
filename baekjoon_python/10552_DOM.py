import sys

input = sys.stdin.readline

# 노인 수, 채널 수, 현재 채널
N, M, P = map(int, input().rstrip().split())
channels = [0 for _ in range(M + 1)]

for _ in range(N):
    # 선호채널, 비선호채널
    a, b = map(int, input().rstrip().split())
    if not channels[b]:
        channels[b] = a

# visited = []
count = 0
while True:
    # if P in visited:
    if count > N:
        print(-1)
        exit()
    elif channels[P]:
        # visited.append(P)
        P = channels[P]
        count += 1
    else:
        break

print(count)

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = []
for _ in range(0, N):
    arr.append(list(map(int, input().split())))

for i in range(0, N):
    for j in range(0, M):
        if arr[i][j] == 4:
            start_i = i
            start_j = j
        elif arr[i][j] == 3:
            if i-1 >= 0:
                arr[i-1][j] = 1
                if j-1 >= 0:
                    arr[i-1][j-1] = 1
                elif j+1 < M:
                    arr[i-1][j+1] = 1
            if j-1 >= 0:
                arr[i][j-1] = 1
            elif j+1 < M:
                arr[i][j+1] = 1
            if i+1 < N:
                arr[i+1][j] = 1
                if j-1 >= 0:
                    arr[i+1][j-1] = 1
                elif j+1 < M:
                    arr[i+1][j+1] = 1
        elif arr[i][j] == 2:
            finish_i = i
            finish_j = j
count = 0
head = 0, 1, 2, 3  # 0:up 1:down 2:left 3:right

if finish_i - start_i > 0:
    head = 1
elif finish_i - start_i < 0:
    head = 0
else:
    if start_j - finish_j > 0:
        head = 3
    else:
        head = 2
while start_i != finish_i and start_j != finish_j:
    if head == 0:
        if arr[start_i-1][start_j] == 0:
            arr[start_i][start_j]
            start_i = start_i-1
            count += 1
        elif arr[start_i][start_j-1] == 0:
            start_j = start_j-1
            count += 1
        elif arr[start_i][start_j+1] == 0:
            start_j = start_j+1
            count += 1
        elif arr[start_i+1][start_]

print(count)

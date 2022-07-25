import sys
input = sys.stdin.readline

size = 19  # 바둑판 가로,세로 사이즈

field = [list(map(int, input().split())) for _ in range(size)]

dx = [1, 0, 1, 1]  # 오른쪽, 아래, 오른쪽위, 오른쪽아래
dy = [0, 1, -1, 1]

for y in range(size):
    for x in range(size):
        if field[y][x]:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                count = 1

                if nx < 0 or ny < 0 or nx >= size or ny >= size:
                    continue

                while 0 <= nx < size and 0 <= ny < size and field[y][x] == field[ny][nx]:
                    count += 1

                    if count == 5:
                        if 0 <= nx + dx[i] < size and 0 <= ny + dy[i] < size and field[ny][nx] == field[ny + dy[i]][nx + dx[i]]:
                            break
                        print(field[y][x])
                        print(y+1, x+1)
                        exit()

                    nx += dx[i]
                    ny += dy[i]
print(0)

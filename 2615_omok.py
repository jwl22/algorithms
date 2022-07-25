import sys
input = sys.stdin.readline

size = 19  # 바둑판 가로,세로 사이즈

field = [list(map(int, input().split())) for _ in range(size)]

# 각각 아래/오른쪽/대각선으로 연속되는지 체크할 떄 사용하는 변수
b_right = w_right = b_down = w_down = b_diagonal = w_diagonal = 0
trigger = 0  # 대각선 검사 시 y축 넘어갈 때 한 번만 초기화해주기 위한 변수
winner = 0  # 승자가 흑이면 1, 백이면 2
for i in range(size):
    for j in range(size):
        # 가로 연속 체크
        if field[i][j] == 1:
            if w_right == 5:
                winner = 2
                break
            w_right = 0
            b_right += 1
        elif field[i][j] == 2:
            if b_right == 5:
                winner = 1
                break
            b_right = 0
            w_right += 1
        else:
            if w_right == 5:
                winner = 2
                break
            elif b_right == 5:
                winner = 1
                break
            b_right = 0
            w_right = 0
        # 세로 연속 체크
        if field[j][i] == 1:
            if w_down == 5:
                winner = 2
                break
            w_down = 0
            b_down += 1
        elif field[j][i] == 2:
            if b_down == 5:
                winner = 1
                break
            b_down = 0
            w_down += 1
        else:
            if w_down == 5:
                winner = 2
                break
            elif b_down == 5:
                winner = 1
                break
            b_down = 0
            w_down = 0
        # 대각선 연속 체크
        y, x = j+i, j  # 대각선 검사 시 사용할 변수
        if y >= size:
            y -= size
            trigger += 1
            if trigger == 1:
                w_diagonal = 0
                b_diagonal = 0
        if field[y][x] == 1:
            if w_diagonal == 5:
                winner = 2
                break
            w_diagonal = 0
            b_diagonal += 1
        elif field[y][x] == 2:
            if b_diagonal == 5:
                winner = 1
                break
            b_diagonal = 0
            w_diagonal += 1
        else:
            if w_diagonal == 5:
                winner = 2
                break
            elif b_diagonal == 5:
                winner = 1
                break
            b_diagonal = 0
            w_diagonal = 0
    if winner != 0:
        if winner == 1:
            print(1)
            if b_right == 5:
                print(i+1, j-3)
            elif b_down == 5:
                print(j-3, i+1)
            else:
                print(y-3, x-3)
        elif winner == 2:
            print(2)
            if w_right == 5:
                print(i+1, j-3)
            elif w_down == 5:
                print(j-3, i+1)
            else:
                print(y-3, x-3)
        break
    b_right = 0
    w_right = 0
    b_down = 0
    w_down = 0
    b_diagonal = 0
    w_diagonal = 0

if winner == 0:
    print(0)

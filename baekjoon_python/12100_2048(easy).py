import sys
import copy

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# d_queue = [] #

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))

best = 0
best = max(map(max, board))

def chk(board_copy, d, count):
    
    # if d_queue == [3,0]:
    #     print()
    
    global N, best

    start, end, step = 0, 0, 0
    if d == 0 or d == 2:
        start = 0
        end = N - 1
        step = 1
        tmp_idx = [0 for _ in range(N)]

    elif d == 1 or d == 3:
        start = N - 1
        end = 0
        step = -1
        tmp_idx = [N - 1 for _ in range(N)]


    zero_idx = [-1 for _ in range(N)]

    if d == 0 or d == 1:
        tmp = board_copy[start].copy()
        for i in range(start, end, step):
            for j in range(N):
                if zero_idx[j] == -1 and board_copy[i][j] == 0:
                    zero_idx[j] = i
                if board_copy[i + dy[d]][j + dx[d]] != 0:
                    if board_copy[i + dy[d]][j + dx[d]] != tmp[j]:
                        tmp[j] = board_copy[i + dy[d]][j + dx[d]]
                        tmp_idx[j] = i + dy[d]
                        if zero_idx[j] != -1:
                            board_copy[zero_idx[j]][j], board_copy[i + dy[d]][j + dx[d]] = board_copy[i + dy[d]][
                                j + dx[d]], board_copy[zero_idx[j]][j]
                            tmp_idx[j] = zero_idx[j]
                            zero_idx[j] = tmp_idx[j] + dy[d]
                    else:
                        board_copy[tmp_idx[j]][j] *= 2
                        if board_copy[tmp_idx[j]][j] > best:
                            best = board_copy[tmp_idx[j]][j]
                        board_copy[i + dy[d]][j + dx[d]] = 0
                        tmp[j] = board_copy[tmp_idx[j]+dy[d]][j+dx[d]]
                        tmp_idx[j] = tmp_idx[j]+dy[d]
    else:
        tmp = []
        if d == 2:
            for i in board_copy:
                tmp += [i[0]]
        else:
            for i in board_copy:
                tmp += [i[N - 1]]
        for i in range(start, end, step):
            for j in range(N):
                if zero_idx[j] == -1 and board_copy[j][i] == 0:
                    zero_idx[j] = i
                if board_copy[j + dy[d]][i + dx[d]] != 0:
                    if board_copy[j + dy[d]][i + dx[d]] != tmp[j]:
                        tmp[j] = board_copy[j + dy[d]][i + dx[d]]
                        tmp_idx[j] = i + dx[d]
                        if zero_idx[j] != -1:
                            board_copy[j][zero_idx[j]], board_copy[j + dy[d]][i + dx[d]] = board_copy[j + dy[d]][
                                i + dx[d]], board_copy[j][zero_idx[j]]
                            tmp_idx[j] = zero_idx[j]
                            zero_idx[j] = tmp_idx[j] + dx[d]
                    else:
                        board_copy[j][tmp_idx[j]] *= 2
                        if board_copy[j][tmp_idx[j]] > best:
                            best = board_copy[j][tmp_idx[j]]
                        board_copy[j + dy[d]][i + dx[d]] = 0
                        tmp[j] = board_copy[j+dy[d]][tmp_idx[j]+dx[d]]
                        tmp_idx[j] = tmp_idx[j]+dx[d]

    move(board_copy, count + 1)


def move(board2, count):
    if count == 5:
        return
    for i in range(4):
        # d_queue.append(i)   #
        chk(copy.deepcopy(board2), i, count)
        # d_queue.pop()

move(board, 0)
print(best)
import sys
import math
input = sys.stdin.readline

T = int(input())
solve_list = []

for _ in range(0, T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    circle_distance = math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2))

    if x1 == x2 and y1 == y2 and r1 == r2:
        if r1 == r2 == 0:
            solve_list.append(1)
        else:
            solve_list.append(-1)
    elif circle_distance == r1+r2:
        solve_list.append(1)
    elif circle_distance < r1+r2:
        if circle_distance < r1 or circle_distance < r2:
            if r1 == r2+circle_distance or r1+circle_distance == r2:
                solve_list.append(1)
            elif (circle_distance+r1 > r2 and r1 <= r2) or (circle_distance+r2 > r1 and r1 >= r2):
                solve_list.append(2)
            else:
                solve_list.append(0)
        else:
            solve_list.append(2)
    else:
        solve_list.append(0)

for i in solve_list:
    print(i)

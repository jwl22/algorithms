# import sys
# from collections import deque
# input = sys.stdin.readline

# tmp = []
# zeros = deque()
# N = int(input())
# idx = 0
# for _ in range(N):
#     x = int(input())
#     if x != 0:
#         tmp.append([x, idx])
#     else:
#         zeros.append(idx)
#     idx += 1

# tmp = sorted(tmp)
# for i in zeros:
#     flag = 0
#     for j in range(len(tmp)):
#         if tmp[j][1] < i:
#             print(tmp.pop(j)[0])
#             flag = 1
#             break
#     if flag == 0:
#         print(0)


import sys
import heapq
input = sys.stdin.readline

tmp = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(tmp, x)
    else:
        if tmp:
            print(heapq.heappop(tmp))
        else:
            print(0)

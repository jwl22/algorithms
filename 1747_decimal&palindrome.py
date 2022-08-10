import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    N += 1

while True:
    flag = 0
    N_str = str(N)
    for i in range(len(N_str)):
        if i >= len(N_str)/2:
            break
        if N_str[i] != N_str[len(N_str)-1-i]:
            flag = 1
            break
    if flag == 1:
        N += 1
        continue
    for i in range(2, N):
        # if i > N/2:
        #     break
        if N % i == 0:
            flag = 1
            break
    if flag == 1:
        N += 1
        continue
    print(N)
    exit()

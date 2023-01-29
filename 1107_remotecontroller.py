import sys

input = sys.stdin.readline

N = int(input())  # 이동하려 하는 채널
M = int(input())  # 고장난 버튼 수
if M != 0:
    broken = input().rstrip().split()  # 고장난 버튼
    if M == 10:
        print(abs(100-N))
        exit()
else:
    print(min(len(str(N)), abs(N - 100)))
    exit()

curchannel_up = N
curchannel_down = N
if N == 100:
    print(0)
    exit()
count_up = len(str(N))
count_down = len(str(N))
isdupl_up = 0
isdupl_down = 0

while True:
    channel_down = list(str(curchannel_down))

    idx = 0
    flag = 0
    for i in channel_down:
        idx += 1
        if i in broken:
            flag = 1
            for j in range(1, len(channel_down) - idx + 1):
                count_down += curchannel_down % (10 ** j)
                curchannel_down -= curchannel_down % (10**j)
            curchannel_down -= 1
            channel_down_after = list(str(curchannel_down))
            if len(channel_down_after) == len(channel_down):
                count_down += 1
            break
    if curchannel_down < 0:
        count_down = abs(N - 100) + 1   # 절대 체택되지 않도록
        break
    if flag == 0:
        break

while True:
    channel_up = list(str(curchannel_up))

    idx = 0
    flag = 0
    for i in channel_up:
        idx += 1
        if i in broken:
            flag = 1
            # curchannel_up += 10 ** (len(channel_up) - idx)
            # count_up += 10 ** (len(channel_up) - idx)
            count_up += (10 ** (len(channel_up) - idx)) - curchannel_up % (10 ** (len(channel_up) - idx))
            curchannel_up += (10 ** (len(channel_up) - idx)) - curchannel_up % (10 ** (len(channel_up) - idx))
            channel_up_after = list(str(curchannel_up))
            if len(channel_up_after) != len(channel_up):
                count_up += 1
            break

    if count_up > count_down:
        break
    if flag == 0:
        break
# print(curchannel_down, curchannel_up)
# print(count_down, count_up)
print(min(count_down, count_up, abs(N - 100)))

from collections import deque
import sys
input = sys.stdin.readline

testcase_count = int(input())
result = dict()

for i in range(testcase_count):
    queue = deque()
    result[i] = 1

    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    # 입력받은 리스트 큐로 저장
    for j in num_list:
        queue.append(j)

    while True:
        flag = 0
        for j in queue:
            if queue[0] < j:
                queue.rotate(-1)
                if M == 0:
                    M = len(queue)-1
                else:
                    M -= 1
                flag = 1
                break
        if flag == 0:
            if M == 0:
                break
            else:
                queue.popleft()
                M -= 1
                result[i] += 1
        # if M == 0:
        #     for j in queue:
        #         if queue[M] < j:
        #             queue.rotate(-1)
        #             M = len(queue)-1
        #             break
        #     if M == 0:
        #         break
        # elif queue[M] <= queue.popleft():
        #     M -= 1
        #     result[i] += 1
        # else:
        #     M -= 1

for i in range(testcase_count):
    print(result[i])

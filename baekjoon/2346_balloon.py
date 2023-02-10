from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

change_list = list(map(int, input().split()))
change_queue = deque()  # 주어진 순서 변경 숫자들을 큐로 저장
for i in change_list:
    change_queue.append(i)

default_queue = deque()  # 처음 큐의 순서를 저장
for i in range(N):
    default_queue.append(i+1)

result_queue = deque()  # 결과 저장
for _ in range(N):
    result_queue.append(default_queue.popleft())
    change = change_queue.popleft()
    if change < 0:
        default_queue.rotate(-(change))
        change_queue.rotate(-(change))
    else:
        default_queue.rotate(-(change-1))
        change_queue.rotate(-(change-1))

for i in result_queue:
    print(i, end=" ")

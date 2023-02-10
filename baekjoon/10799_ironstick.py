from collections import deque
import sys
input = sys.stdin.readline

parenthesis = input().rstrip()

parenthesis_list = deque()
for i in parenthesis:
    parenthesis_list.append(i)

# flag: ()가 붙어있는지 확인하기 위한 플래그, count: 현재 막대 갯수, result: 총 막대 갯수 계산
flag = count = result = 0
for i in parenthesis_list:
    if i == '(':
        count += 1
        flag = 1  # 직전에 (일 때 flag = 1
    else:
        count -= 1
        if flag == 1:
            result += count
        else:
            result += 1
        flag = 0

print(result)

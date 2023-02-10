from collections import deque
import sys
import re
input = sys.stdin.readline

pattern = re.compile(r'[a-zA-Z]')

N = int(input())
stack = deque()

# 테스트 구문 입력
postfix = input().rstrip()
postfix_list = deque()
for i in postfix:
    postfix_list.append(i)
dic = dict()

# 숫자 입력받아 딕셔너리 저장
postfix_variable_index = 0
for i in range(N):
    value = int(input())
    while not pattern.match(postfix_list[postfix_variable_index]) or postfix_list[postfix_variable_index] in dic:
        postfix_variable_index += 1
    dic[postfix_list[postfix_variable_index]] = value

# 계산
for i in postfix_list:
    if i == "+":
        b = stack.pop()
        a = stack.pop()
        stack.append(a+b)
    elif i == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a-b)
    elif i == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a*b)
    elif i == "/":
        b = stack.pop()
        a = stack.pop()
        stack.append(a/b)
    else:
        stack.append(dic[i])

print('%.2f' % stack[0])

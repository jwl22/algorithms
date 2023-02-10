from collections import deque
import sys
input = sys.stdin.readline

result = flag = small_count = big_count = 0
mul_value = 1

string = input().rstrip()
stack = deque()
try:
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
            flag = 0
            if i == '(':
                mul_value *= 2
                small_count += 1
            else:
                mul_value *= 3
                big_count += 1
        elif i == ')':
            small_count -= 1
            if flag == 0:
                result += mul_value
            flag = 1
            mul_value /= 2
            if stack.pop() != '(':
                result = 0
                break
        elif i == ']':
            big_count -= 1
            if flag == 0:
                result += mul_value
            flag = 1
            mul_value /= 3
            if stack.pop() != '[':
                result = 0
                break
    if big_count != 0 or small_count != 0:
        result = 0
except:
    result = 0


print(int(result))

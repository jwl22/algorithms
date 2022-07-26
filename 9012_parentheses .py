import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    testcase = input()
    testcase_lst = []
    for i in testcase:
        testcase_lst.append(i)

    count = 0
    for i in testcase_lst:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            if count < 0:
                break

    if count == 0:
        print("YES")
    else:
        print("NO")

from itertools import combinations
import sys
input = sys.stdin.readline

exp = [*input().rstrip()]
p_open, p_set = [], []

for i, v in enumerate(exp):
    if v == '(':
        exp[i] = ''
        p_open += [i]
    elif v == ')':
        exp[i] = ''
        p_set += [[p_open.pop(), i]]

printline = set()  # 중복 제거 위한 집합 자료형 사용

for i in range(len(p_set)):
    for j in combinations(p_set, i):
        exp_clone = exp.copy()
        for a, b in j:
            exp_clone[a] = '('
            exp_clone[b] = ')'
        printline.add(''.join(exp_clone))

for i in sorted(printline):
    print(i)

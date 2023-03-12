import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

lst = []
for i in range(1, N + 1):
    lst.append(i)
result = []
idx = 0
while lst:
    idx += K - 1
    while idx >= len(lst):
        idx -= len(lst)
    tmp = lst.pop(idx)
    result.append(tmp)

print('<', end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print('>')

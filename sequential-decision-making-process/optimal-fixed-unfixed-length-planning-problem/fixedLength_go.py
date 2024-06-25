#2018253082 이정우

import sys
input = sys.stdin.readline

LENGTH = 7

states = ['A', 'B', 'C', 'D', 'E']
states_length = len(states)

initial_cost = [[2, 2, -1, -1, -1], # -1 = 없는 경로
               [-1, -1, 1, 4, -1],
               [1, -1, -1, 1, -1],
               [-1, -1, 1, -1, 1],
               [-1, -1, -1, -1, -1]]
cost_to_go = [[-1 for _ in range(states_length)] for _ in range(LENGTH)]

cost_to_go[LENGTH-1][1] = 0

for i in range(LENGTH-2, -1, -1):
    tmp = []
    for j in range(states_length):
        if cost_to_go[i+1][j] != -1:
            tmp.append(j)
    for j in range(states_length):
        for k in tmp:
            if initial_cost[j][k] != -1 and (cost_to_go[i][j] == -1 or cost_to_go[i][j] > cost_to_go[i+1][k] + initial_cost[j][k]):
                cost_to_go[i][j] = cost_to_go[i+1][k] + initial_cost[j][k]

print("Fixed-Length_Cost-to-go")
idx = LENGTH
for i in states:
    print('\t' + i, end=' ')
print()
for i in list(reversed(cost_to_go)):
    print('G' + str(idx), end='\t')
    for j in i:
        if j == -1:
            print('∞',end='\t')
        else:
            print(j, end='\t')
    print()
    idx -= 1
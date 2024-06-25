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
cost_to_come = [[-1 for _ in range(states_length)] for _ in range(LENGTH)]

cost_to_come[0][1] = 0

for i in range(1, LENGTH):
    for j in range(states_length):
        if cost_to_come[i-1][j] != -1:
            for k in range(states_length):
                if initial_cost[j][k] != -1:
                    if cost_to_come[i][k] == -1:
                        cost_to_come[i][k] = initial_cost[j][k] + cost_to_come[i-1][j]
                    else:
                        cost_to_come[i][k] = min(cost_to_come[i-1][j] + initial_cost[j][k], cost_to_come[i][k])

print("Fixed-Length_Cost-to-come")
idx = 1
for i in states:
    print('\t' + i, end=' ')
print()
for i in list(cost_to_come):
    print('C' + str(idx), end='\t')
    for j in i:
        if j == -1:
            print('∞',end='\t')
        else:
            print(j, end='\t')
    print()
    idx += 1
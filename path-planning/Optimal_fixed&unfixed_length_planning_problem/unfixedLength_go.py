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
cost_to_go = [-1 for _ in range(states_length)]

cost_to_go[1] = 0
while True:
    tmp = []
    comp_cost = cost_to_go.copy()
    for i in range(states_length):
        if cost_to_go[i] != -1:
            tmp.append(i)
    for i in range(states_length):
        for j in range(states_length):
            if initial_cost[i][j] != -1 and j in tmp:
                if cost_to_go[i] == -1:
                    cost_to_go[i] = initial_cost[i][j] + cost_to_go[j]
                else:
                    cost_to_go[i] = min(cost_to_go[i], initial_cost[i][j] + cost_to_go[j])
    if cost_to_go == comp_cost:
        break

print("Unfixed-Length_Cost-to-go")

for i in states:
    print('\t' + i, end=' ')
print()
print('G*', end='\t')
for i in cost_to_go:
    if i == -1:
        print('∞',end='\t')
    else:
        print(i, end='\t')
print()
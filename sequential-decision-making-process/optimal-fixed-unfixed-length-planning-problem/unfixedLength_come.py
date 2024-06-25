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
cost_to_come = [-1 for _ in range(states_length)]

cost_to_come[1] = 0
while True:
    comp_cost = cost_to_come.copy()

    for i in range(5):
        if cost_to_come[i] != -1:
            for j in range(5):
                if initial_cost[i][j] != -1:
                    if cost_to_come[j] == -1:
                        cost_to_come[j] = cost_to_come[i] + initial_cost[i][j]
                    else:
                        cost_to_come[j] = min(cost_to_come[i] + initial_cost[i][j], cost_to_come[j])

    if cost_to_come == comp_cost:
        break

print("Unfixed-Length_Cost-to-come")

for i in states:
    print('\t' + i, end=' ')
print()
print('G*', end='\t')
for i in cost_to_come:
    if i == -1:
        print('∞',end='\t')
    else:
        print(i, end='\t')
print()
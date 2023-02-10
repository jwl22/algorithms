from collections import deque
import sys
import copy
input = sys.stdin.readline

dot = dict()
# line = deque()
answer = deque()


# def isarticulation(tree, idx, queue):
#     for i in tree[idx]:
#         queue.append(i)
#         tree[i].remove(idx)
#         isarticulation(tree, i, queue)


N = int(input())  # 점의 개수
for i in range(1, N+1):  # 딕셔너리 리스트로 초기화
    dot[i] = []
for _ in range(N-1):
    a, b = map(int, input().split())
    # line.append([a, b])
    dot[a].append(b)
    dot[b].append(a)

q = int(input())  # 질문의 개수
for _ in range(q):
    # dot2 = copy.deepcopy(dot)
    t, k = map(int, input().split())
    if t == 1:  # 단절점인지 검사
        if len(dot[k]) == 1:
            answer.append('no')
        else:
            answer.append('yes')
        # for i in dot2[k]:
        #     dot2[i].remove(k)
        # for i in dot2[k]:
        #     search = []
        #     search.append(i)
        #     isarticulation(dot2, i, search)
        #     search = list(set(search))
        #     if len(search) == N-1:
        #         answer.append('no')
        #         break
        # if len(search) != N-1:
        #     answer.append('yes')
        # dot2[k] = []

    elif t == 2:  # 단절선인지 검사
        answer.append('yes')
        # dot2[line[k-1][0]].remove(line[k-1][1])
        # dot2[line[k-1][1]].remove(line[k-1][0])
        # for i in range(2):
        #     search = []
        #     search.append(line[k-1][i])
        #     isarticulation(dot2, line[k-1][i], search)
        #     search = list(set(search))
        #     if len(search) == N:
        #         answer.append('no')
        #         break
        # if len(search) != N:
        #     answer.append('yes')

for i in answer:
    print(i)

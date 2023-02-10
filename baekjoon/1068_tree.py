from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))
delete = root = int(input())

child = []
for i in range(N):
    child.append([])

# 각 노드 번호에 연결된 자식들 저장
index = 0
for i in parent:
    if i != -1:
        child[i].append(index)
    else:
        root = index
    index += 1

# 자식 노드 삭제
deletes = deque()
if parent[delete] != -1:
    child[parent[delete]].remove(delete)
deletes.append(delete)
while deletes:
    delete_index = deletes.pop()
    while child[delete_index]:
        deletes.append(child[delete_index].pop())

# 자식 없는 노드 카운팅하여 출력
if delete != root and not child[root]:
    count = 1
else:
    count = 0
    for i in child:
        if i:
            for j in i:
                if not child[j]:
                    count += 1
print(count)

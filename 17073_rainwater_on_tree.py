import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, W = map(int, input().split())

count = 0


def count_lastnode(tree, parent):
    global count
    for i in tree[parent]:
        tree[i].remove(parent)
        if len(tree[i]) == 0:
            count += 1
            continue
        count_lastnode(tree, i)


tree = dict()
for i in range(1, N+1):
    tree[i] = []

for _ in range(0, N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

count_lastnode(tree, 1)
print(W/count)

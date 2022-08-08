from collections import deque
import sys
input = sys.stdin.readline

tree, tree2 = {}, {}
nodes = []
count = 1  # 루트 노드 1개를 기본으로
node_count = 0
result = deque()


def finding(root):
    global count
    for i in tree2[root]:
        finding(i)
        count += 1


def istree():
    global tree2
    tree_len = len(nodes)
    nodezero_count = 0
    while nodes:
        node = nodes.pop()
        try:
            if len(tree[node]) != 1:
                result.append(0)
                nodes.clear()
                return
        except:
            root = node
            nodezero_count += 1
            if nodezero_count > 1:
                result.append(0)
                nodes.clear()
                return
    if nodezero_count == 0:
        result.append(0)
        nodes.clear()
        return

    for key, v in tree.items():
        for i in v:
            tree2[i].append(key)

    finding(root)

    if tree_len != node_count:
        result.append(0)
        nodes.clear()
        return
    result.append(1)


while True:
    line = list(map(int, input().split()))
    exit_flag = reset_flag = odd = node = 0
    for i in line:
        odd += 1
        if i == -1:
            if exit_flag == 1:
                case = 1
                for i in result:
                    if i == 0:
                        print('Case', case, 'is not a tree.')
                    else:
                        print('Case', case, 'is a tree.')
                    case += 1
                exit()
            exit_flag = 1
        elif i == 0:
            if reset_flag == 1:
                if len(nodes) == 0:
                    result.append(1)
                else:
                    nodes = list(set(nodes))
                    node_count = len(nodes)
                    for i in nodes:
                        tree2[i] = []
                    istree()
                    tree2, tree = {}, {}
                    count = 1
                    node_count = 0
            reset_flag = 1
        else:
            nodes.append(i)
            exit_flag = reset_flag = 0

            if odd % 2 == 0:
                try:
                    tree[i].append(node)
                except:
                    tree[i] = [node]
            else:
                node = i

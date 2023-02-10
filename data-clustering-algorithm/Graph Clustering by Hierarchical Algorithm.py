# 약 8분정도 소요되며 파일로 출력되는 결과와 별개로 터미널에 출력되는 값은 threshold값입니다.

import sys
import copy
from collections import deque
input = sys.stdin.readline
if __name__ == '__main__':

    def dfs(graph, start, visited=[]):
        visited.append(start)

        for node in graph[start]:
            if node not in visited:
                dfs(graph, node, visited)
        return visited

    ## 파일 읽어오기
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    fd = []
    for line in lines:
        fd.append(line.split('\t'))  # fd[로우][칼럼]

    r = len(fd)
    c = len(fd[0])
    ##
    cluster = dict()  # gen id별로 연결된 vertex들
    for i in fd:  # 라인
        # for j in i: #gene ID 하나
        if i[0] in cluster:
            if i[1] not in cluster[i[0]]:
                cluster[i[0]].append(i[1])
        else:
            cluster[i[0]] = [i[1]]
        if i[1] in cluster:
            if i[0] not in cluster[i[1]]:
                cluster[i[1]].append(i[0])
        else:
            cluster[i[1]] = [i[0]]

    ## 초기 서브그래프들 탐색
    graph_visited = []
    graph_list = []
    for i in cluster:  # 모든 vertex 순차 탐색
        if i in graph_visited:
            continue
        dfs_result = []
        dfs(cluster, i, dfs_result)
        # dfs_result = bfs(cluster, i)
        graph_visited += dfs_result
        graph_list.append(dfs_result)
    graph_count = len(graph_list)
    ##

    ## 덴시티 쓰레스홀드 0.4이상인지 확인
    result = []
    for i in range(len(graph_list)):
        tmp = []
        edge = 0
        for j in graph_list[i]:
            edge += len(cluster[j])
            for k in tmp:
                if k in cluster[j]:
                    edge -= 1
            tmp.append(j)
        threshold = (2 * edge) / (len(graph_list[i]) * (len(graph_list[i]) - 1))
        if threshold >= 0.4:
            result.append(graph_list[i])
            graph_list[i] = []
    graph_list_tmp = []
    for i in graph_list:
        if i:
            graph_list_tmp.append(i)
    graph_list = graph_list_tmp
    ##

    ## 서브그래프별로 제이카드 코에피션트가 가장 낮은 값 찾아 삭제
    count = 0
    cluster_copy = copy.deepcopy(cluster)
    while True:
        if not graph_list:
            break
        # count += 1
        graph_idx = 0

        # graph_list_tmp = []
        # for j in graph_list:
        #     if j:
        #         graph_list_tmp.append(j)
        # graph_list = graph_list_tmp

        if graph_idx >= len(graph_list):
            break
        else:
            i = graph_list[graph_idx]

        # for i in graph_list:    # 서브그래프 순환
        jaccard_coef = 2
        jaccard_vertex = []
        for j in i:  # 하나의 서브그래프의 버텍스들 탐색
            flag = 0
            for k in i:
                if j == k:
                    flag = 1
                    continue
                if flag == 0 or (k not in cluster_copy[j]):
                    continue
                # for k in cluster[j]:    # 그 하나의 버텍스와 연결된 버텍스 탐색
                totaledge = list(set().union(cluster_copy[j], cluster_copy[k]))
                sameedge = list(set(cluster_copy[j]).intersection(cluster_copy[k]))
                if j < k:
                    jaccard_vertex.append([len(sameedge) / len(totaledge), j, k])
                else:
                    jaccard_vertex.append([len(sameedge) / len(totaledge), k, j])
                # if len(sameedge) / len(totaledge) < jaccard_coef:
                #     jaccard_coef = len(sameedge) / len(totaledge)
                #     jaccard_vertex = [[j, k]]
                # elif len(sameedge) / len(totaledge) == jaccard_coef:
                #     jaccard_vertex.append([j, k])
        jaccard_vertex.sort()
        # for i in jaccard_vertex:
        #     print(i)

        idx = 0
        # print(len(jaccard_vertex))
        while True:
            cluster_copy[jaccard_vertex[idx][1]].remove(jaccard_vertex[idx][2])
            cluster_copy[jaccard_vertex[idx][2]].remove(jaccard_vertex[idx][1])
            # dfs_result = []
            # dfs(cluster_copy, jaccard_vertex[idx][0], dfs_result)
            dfs_result = []
            queue = deque()
            queue.append(jaccard_vertex[idx][1])
            flag_find = 0
            while queue:
                node = queue.popleft()
                if node == jaccard_vertex[idx][2]:
                    # dfs_result.append(node)
                    flag_find = 1
                    break
                if node not in dfs_result:
                    dfs_result.append(node)
                    queue.extend(cluster_copy[node])
            # dfs_result = bfs(cluster_copy, jaccard_vertex[idx][0])
            # if jaccard_vertex[idx][1] not in dfs_result:
            if flag_find == 0:
                graph_list[graph_idx] = list(set(graph_list[graph_idx]).difference(dfs_result))
                if len(graph_list[graph_idx]) < len(dfs_result):
                    graph_list[graph_idx], dfs_result = dfs_result, graph_list[graph_idx]
                if len(dfs_result) == 1:
                    result.append(dfs_result)
                elif len(graph_list[graph_idx]) == 1:
                    result.append(graph_list[graph_idx])
                    # graph_list.pop(graph_idx)
                    # graph_list[graph_idx] = []
                    graph_list.pop(graph_idx)
                    graph_idx -= 1
                    result.append(dfs_result)
                    break
                else:
                    tmp = []
                    edge = 0
                    for j in dfs_result:
                        edge += len(cluster_copy[j])
                        for k in tmp:
                            if k in cluster_copy[j]:
                                edge -= 1
                        tmp.append(j)
                    threshold = (2 * edge) / (len(dfs_result) * (len(dfs_result) - 1))
                    if threshold >= 0.4:
                        result.append(dfs_result)
                    else:
                        graph_list.append(dfs_result)

                tmp = []
                edge = 0
                for j in graph_list[graph_idx]:
                    edge += len(cluster_copy[j])
                    for k in tmp:
                        if k in cluster_copy[j]:
                            edge -= 1
                    tmp.append(j)
                threshold = (2 * edge) / (len(graph_list[graph_idx]) * (len(graph_list[graph_idx]) - 1))
                if threshold >= 0.4:
                    result.append(graph_list[graph_idx])
                    # graph_list[i] = []
                    graph_list.pop(graph_idx)
                    graph_idx -= 1
                print(threshold)

                break
            idx += 1
        graph_idx += 1

    result.sort(key=lambda x: len(x), reverse=True)
    sys.stdout = open('assignment6_output.txt', 'w')
    for i in result:
        if len(i) >= 10:
            print(str(len(i)) + ':', end=' ')
            for j in i:
                print(j, end=' ')
            print()
    sys.stdout.close()

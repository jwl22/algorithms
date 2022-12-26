#주기적으로 남은 edge수가 프린트되며, i5-1135G7 기준 약 5분 소요됩니다.
import sys
import copy
from collections import deque

clique_result = []  #전체 벌텍스 연결 상태

def file_open():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in lines]
        fd = []
        for line in lines:
            x = line.strip().split('\t')
            fd.append(x)  # fd[로우][칼럼]

        return fd

def create_dict(fd, connect):
    global clique_result

    for i in fd:  # 라인
        clique_result.append([i[0], i[1]])
        if i[0] in connect:
            if i[1] not in connect[i[0]]:
                connect[i[0]].append(i[1])
        else:
            connect[i[0]] = [i[1]]
        if i[1] in connect:
            if i[0] not in connect[i[1]]:
                connect[i[1]].append(i[0])
        else:
            connect[i[1]] = [i[0]]

def overlap_del(list):
    global clique_result

    if list in clique_result:
        clique_result.remove(list)

def maximal(cluster):
    global clique_result

    clique = []
    # 3clique 탐색 및 리스트 저장
    for i in cluster:   # cluster[i]. 하나의 vertex에 연결된 vertex 리스트
        if len(cluster[i])>=2:
            for j in cluster[i]:
                flag = 0
                for k in cluster[i]:
                    if j==k:
                        flag = 1
                        continue
                    if flag == 0:
                        continue
                    if j in cluster[k]:
                        if [i,j,k] not in clique and [i,k,j] not in clique and [j,i,k] not in clique and [j,k,i] not in clique and [k,i,j] not in clique and [k,j,i] not in clique:
                            clique.append([i,j,k])

                            overlap_del([i, j])
                            overlap_del([j, i])
                            overlap_del([j, k])
                            overlap_del([k, j])
                            overlap_del([i, k])
                            overlap_del([k, i])
                            clique_result.append([i, j, k])
    clique_up = []
    while True:
        if not clique:
            break

        clique_up = []
        clique_len = len(clique[0])
        for i in clique:    # 클리크 한 줄
            flag = 0
            for j in clique:
                samecount = 0
                isdiff = False
                if i == j:
                    flag = 1
                    continue
                if flag == 0:
                    continue
                for k in j:
                    if k in i:
                        samecount += 1
                    else:
                        if isdiff == True:  #두 클리크 중 다른게 두 개 이상으로 판명되면 패스
                            break
                        isdiff = True
                if samecount == clique_len-1:
                    diffvertex_i = ''
                    diffvertex_j = ''
                    for k in i:
                        if k not in j:
                            diffvertex_i = k
                            break
                    for k in j:
                        if k not in i:
                            diffvertex_j = k
                            break
                    if diffvertex_i in cluster[diffvertex_j]:
                        appendlist = i.copy()
                        appendlist.append(diffvertex_j)
                        appendlist.sort()
                        if appendlist not in clique_up:
                            clique_up.append(appendlist)
                            result_copy = copy.deepcopy(clique_result)

                            for oneclique in result_copy:
                                cl_count = 0
                                for m in oneclique:
                                    if m not in appendlist:
                                        cl_count += 1
                                        break
                                if cl_count == 0:
                                    clique_result.remove(oneclique)
                            clique_result.append(appendlist)

        clique = clique_up.copy()


    clique_result.sort(key=lambda x: len(x), reverse=True)
    if clique_result:
        return clique_result[0]
    else:
        return 'end'

def clustering(cluster, clique_result_bak, connect):
    global clique_result

    while True:
        clique_result = copy.deepcopy(clique_result_bak)
        maximal_clique = maximal(connect)  # Maximum 클리크 하나
        print(len(clique_result_bak))   # 남은 edge 수
        if maximal_clique == 'end':
            break

        edge_count = (len(maximal_clique) * (len(maximal_clique) - 1)) / 2  # 맥시멀 클리크의 엣지 수
        while True:
            visited = deque()
            best_vertex = ''
            best_diff = 10
            best_count = 0
            E1 = edge_count

            V = len(maximal_clique)
            dencity = (2 * E1) / (V * (V - 1))
            for i in maximal_clique:
                for j in connect[i]:
                    if j in visited:
                        continue
                    visited.append(j)

                    if j in maximal_clique:
                        continue
                    count = 0
                    for k in connect[j]:
                        if k in maximal_clique:
                            count += 1  # 해당 vertex와 클러스터간 연결된 엣지 수
                    E2 = E1 + count
                    V = len(maximal_clique)
                    den_diff = ((2 / V) * (
                            (V * (E1 - E2) + (E1 + E2)) / (V ** 2 - 1)))
                    den_diff = V * (den_diff / dencity) #기존 dencity로 정규화. 다만 클러스터가 커졌을 때는 density 감소 비율이 무조건 작게 나오므로 가중치로 Vertex수를 곱해준다.
                    # print(f"DensityDefferent: {round(den_diff,2)}, AddEdge: {count}")

                    if den_diff < best_diff:
                        best_diff = den_diff
                        best_vertex = j
                        best_count = count
            if best_diff < 1.05:
                edge_count += best_count
                maximal_clique.append(best_vertex)
            else:
                for i in maximal_clique:
                    flag = 0
                    for j in maximal_clique:
                        if i == j:
                            flag = 1
                            continue
                        if flag == 1:
                            if j in connect[i]:
                                connect[i].remove(j)
                                connect[j].remove(i)
                                try:
                                    clique_result_bak.remove([i, j])
                                except:
                                    clique_result_bak.remove([j, i])
                cluster.append(maximal_clique)
                break

def file_print(fileName):
    sys.stdout = open(fileName, 'w')
    for i in cluster:
        print(str(len(i)) + ':', end=' ')
        for j in i:
            print(j, end=' ')
        print()
    sys.stdout.close()

## 파일 읽어와서 라인별 리스트 저장
fd = file_open()

## input file의 edge가 연결된 dictionary 생성
connect = dict()  # gen id별로 연결된 vertex들
create_dict(fd, connect)
clique_result_bak = copy.deepcopy(clique_result)    # maximal함수에서 바뀌기 전에 백업

cluster = []    # 클러스터링 결과 저장
clustering(cluster, clique_result_bak, connect)   # 클러스터링 수행
cluster.sort(key=lambda x: len(x), reverse=True)

outFileName = "clustering.txt"
file_print(outFileName)
import collections
import math
import sys
import time

if __name__ == '__main__':
    start_time = time.process_time() * 1000

    # sys.stdout = open('assignment4_output1.txt', 'w')
    ## 파일 읽어오기
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    fd = []
    for line in lines:
        fd.append(line.split('\t')) #fd[로우][칼럼]

    r = len(fd)
    c = len(fd[0])
    for i in range(r):
        fd[i] = list(map(float, fd[i]))
    ##

    # 각 점 사이의 거리 저장
    dist_obj = [[0 for i in range(r)] for i in range(r)]    #각 로우의 다른 오브젝트간의 거리 dist_obj[r][r]
    cluster_index = []     #클러스터로 사용될 오브젝트의 IndexNo.
    for i in range(r):
        for j in range(r):
            csum = 0
            if i == j:
                continue
            for l in range(c):
                csum += (fd[i][l] - fd[j][l])**2
            dist_obj[i][j] = round(math.sqrt(csum), 3)

    cluster_single = dict()  # 각 클러스터ID별 들어간 유전자ID 저장
    cluster_complete = dict()
    for i in range(r):
        cluster_single[i] = [i]
        cluster_complete[i] = [i]
    ##

    #각 클러스터간의 거리 중 가장 가까운 두 개를 merge
    isDone_single = 0
    isDone_complete = 0

    single_dist = 10000
    complete_dist = 10000

    while True:
        if isDone_single == 0:
            # single distance 클러스터 계산
            single_dist = 10000

            cluster_from = -1  # 이동 할 클러스터 idx
            cluster_to = -1  # 도착 할 클러스터 idx
            for i in cluster_single:
                flag = 0
                for k in cluster_single:  # 클러스터 속 점 하나에 대해 다른 클러스터들과의 거리를 구한다.
                    if i == k:
                        flag = 1
                        continue
                    if flag == 0:
                        continue
                    single_dist_cluster = 10000  # 하나의 클러스터에 대해 다른 클러스터와 거리 계산 시의 최소값
                    for j in cluster_single[i]:  # 해당 클러스터에 들어간 점 하나
                        for l in cluster_single[k]:
                            if dist_obj[j][l] < single_dist_cluster:
                                single_dist_cluster = dist_obj[j][l]
                    if single_dist > single_dist_cluster:
                        single_dist = single_dist_cluster
                        cluster_from = k
                        cluster_to = i
            if single_dist < 5:
                cluster_single[cluster_to] += cluster_single[cluster_from]
                del cluster_single[cluster_from]
            else:
                isDone_single = 1

        if isDone_complete == 0:
            complete_dist = 10000

            # complete distance 클러스터 계산
            cluster_from = -1  # 이동 할 클러스터 idx
            cluster_to = -1  # 도착 할 클러스터 idx
            for i in cluster_complete:
                flag = 0
                for j in cluster_complete:
                    if i == j:
                        flag = 1
                        continue
                    if flag == 0:
                        continue
                    complete_dist_cluster = 0
                    for k in cluster_complete[i]:
                        for l in cluster_complete[j]:
                            if dist_obj[k][l] > complete_dist_cluster:
                                complete_dist_cluster = dist_obj[k][l]
                    if complete_dist > complete_dist_cluster:
                        complete_dist = complete_dist_cluster
                        cluster_from = j
                        cluster_to = i
            if complete_dist < 5:
                cluster_complete[cluster_to] += cluster_complete[cluster_from]
                del cluster_complete[cluster_from]
            else:
                isDone_complete = 1

        if isDone_complete and isDone_single:
            end_time = time.process_time() * 1000
            sys.stdout = open('assignment4_output1.txt', 'w')
            for i in cluster_single:
                print(len(cluster_single[i]), ':', end=' ')
                for j in cluster_single[i]:
                    print(j, end=' ')
                print()
            print('time : ', end_time - start_time, 'ms')
            sys.stdout.close()
            sys.stdout = open('assignment4_output2.txt', 'w')
            for i in cluster_complete:
                print(len(cluster_complete[i]), ':', end=' ')
                for j in cluster_complete[i]:
                    print(j, end=' ')
                print()
            print('time : ', end_time - start_time, 'ms')
            sys.stdout.close()
            break
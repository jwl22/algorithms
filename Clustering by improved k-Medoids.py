import math
import sys
import time

if __name__ == '__main__':
    start_time = time.process_time() * 1000

    sys.stdout = open('assignment3_output.txt', 'w')
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    fd = []
    for line in lines:
        fd.append(line.split('\t')) #fd[로우][칼럼]

    k = 10
    r = len(fd)
    c = len(fd[0])
    for i in range(r):
        fd[i] = list(map(float, fd[i]))

    #초기 클러스터 지정
    dist_obj = [0 for i in range(r)]    #각 로우의 다른 오브젝트간의 거리 합
    cluster_index = []     #클러스터로 사용될 오브젝트의 IndexNo.
    count = 0
    for i in range(r):
        for j in range(r):
            csum = 0
            if i == j:
                continue
            for l in range(c):
                csum += (fd[i][l] - fd[j][l])**2
            dist_obj[i] += math.sqrt(csum)

    sorted_dist_obj = sorted(dist_obj)
    for i in range(k):
        cluster_index.append(dist_obj.index(sorted_dist_obj[i]))

    cluster = dict()  # 각 클러스터ID별 들어간 유전자ID 저장
    cluster_prev = cluster.copy()

    # 각 k클러스터와의 거리 계산해서 가장 가까운 클러스터에 배치
    while True:
        for i in range(k):
            cluster[i] = []
        fd_cluster = [0 for i in range(r)]  # 각 로우별로 들어간 클러스터의 넘버 저장
        for i in range(r):
            distance_tmp = [0 for k_i in range(k)]  # k개의 중심 오브젝트와 하나의 row 사이 거리를 저장할 임시 리스트
            for j in range(c):  # 칼럼 각각과 k개의 클러스터 사이의 거리를 모두 합산함
                for l in range(k):
                    distance_tmp[l] += (fd[i][j] - fd[cluster_index[l]][j]) ** 2
                    distance_tmp[l] = round(distance_tmp[l], 3)
            distance_min = 10000  # 거리의 최솟값 설정. 가장 낮은 값을 구하기 위해 높게 설정한 임의의 10000이라는 값으로 지정.
            cluster_index_2 = -1
            for j in range(k):
                distance_tmp[j] = round(math.sqrt(distance_tmp[j]), 3)
                if distance_tmp[j] < distance_min:
                    distance_min = distance_tmp[j]
                    cluster_index_2 = j
            fd_cluster[i] = cluster_index_2
        for j in range(r):
            cluster[fd_cluster[j]].append(j)
        if cluster_prev == cluster:
            end_time = time.process_time() * 1000
            for i in range(k):
                print(len(cluster[i]), ':', end=' ')
                for j in cluster[i]:
                    print(j, end=' ')
                print()
            print('time : ', end_time - start_time, 'ms')
            sys.stdout.close()
            break
        cluster_prev = cluster.copy()

        # 중심점 재설정
        idx_dist = [0 for i in range(k)]

        for i in range(k):  #클러스터 순환
            min_dist = 10000
            for j in cluster[i]:    #해당 클러스터에 있는 오브젝트idx값 순환
                cluster_dist = 0
                for l in cluster[i]:
                    distance = 0
                    if j == l:
                        continue
                    for m in range(c):
                        distance += (fd[j][m] - fd[l][m])**2
                    cluster_dist += math.sqrt(distance)
                if min_dist > cluster_dist:
                    min_dist = cluster_dist
                    idx_dist[i] = j

        cluster_index = idx_dist.copy()
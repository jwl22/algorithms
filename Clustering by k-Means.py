# 코드 실행 시 약 20초의 시간이 소요됩니다. (round로 소수점 잘라내는 과정에서 발생하는 지연)
import math
import sys
import pandas as pd

if __name__ == '__main__':
    fd = pd.read_csv(sys.argv[1], sep='\t', header=None, encoding='cp949')  # fd[칼럼][로우]
    sys.stdout = open('assignment2_output.txt', 'w')

    k = 10
    r = len(fd.index)
    c = len(fd.columns)
    mean = [[0 for i in range(c)] for i in range(k)]

    # 초기값 설정
    for j in range(c):
        rowsum = [0 for i in range(k)]  # 각 칼럼별로 합을 넣을 리스트. rowsum[k]
        for i in range(r):
            rowsum[i // 50] += float(fd[j][i])
        for i in range(k):
            mean[i][j] += round(rowsum[i] / 50, 3)  # 50개씩 10개로 쪼갠 칼럼별 평균값. mean[k][c]

    distance_prev = 0
    cluster = dict()  # 각 클러스터ID별 들어간 유전자ID 저장
    for i in range(k):
        cluster[i] = []
    # K-mean 클러스터링
    while True:
        df_cluster = [0 for i in range(r)]  # 각 점이 들어간 클러스터의 넘버 저장
        distance = 0
        for i in range(r):
            distance_tmp = [0 for i in range(k)]  # k개의 mean과 하나의 row 사이 거리를 저장할 임시 리스트
            for j in range(c):  # 칼럼 각각과 k개의 클러스터 사이의 거리를 모두 합산함
                for l in range(k):
                    distance_tmp[l] += (fd[j][i] - mean[l][j]) ** 2
                    distance_tmp[l] = round(distance_tmp[l],3)
            distance_min = 10000  # 거리의 최솟값 설정. 가장 낮은 값을 구하기 위해 높게 설정한 임의의 10000이라는 값으로 지정.
            cluster_index = -1
            for j in range(k):
                distance_tmp[j] = round(math.sqrt(distance_tmp[j]),3)
                if distance_tmp[j] < distance_min:
                    distance_min = distance_tmp[j]
                    cluster_index = j
            df_cluster[i] = cluster_index
            distance += distance_min
            distance = round(distance,3)
        if distance_prev == distance:
            for i in range(r):
                cluster[df_cluster[i]].append(i)
            for i in range(k):
                print(len(cluster[i]), ':', end=' ')
                for j in cluster[i]:
                    print(j, end=' ')
                print()
            sys.stdout.close()
            break
        distance_prev = distance

        # 중심점 재설정
        for j in range(c):
            idx_sum = [0 for i in range(k)] #idx_sum[클러스터 No.]. 각 클러스터에 들어간 점들의 전체 값 합산 저장용 리스트
            idx_count = [0 for i in range(k)]
            for i in range(r):
                idx_sum[df_cluster[i]] += fd[j][i]
                idx_sum[df_cluster[i]] = round(idx_sum[df_cluster[i]], 3)
                idx_count[df_cluster[i]] += 1
            for i in range(k):
                mean[i][j] = round(idx_sum[i]/idx_count[i], 3)
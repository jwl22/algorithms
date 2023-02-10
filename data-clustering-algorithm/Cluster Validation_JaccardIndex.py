# 터미널에서 python assignmentEC.py {출력파일} assignment_EC_input 로 하나씩 입력받습니다. (4개 전부 하려면 4번의 실행 필요)
# 소수점 셋째자리에서 반올림된 둘째자리까지 %로 결과가 나옵니다. 세부 결과를 보려면 마지막부분 round부분을 제거하면 됩니다.
# assignment5_output.txt는 각 클러스터링 결과에 대한 계산 결과 값입니다.
# 이전 과제들 결과물 출력 중 시간 결과로 마지막줄에 'ms'나''time'이 포함되어야 해당 라인을 제거하고 탐색합니다.

import sys

if __name__ == '__main__':
    # sys.stdout = open('assignment4_output1.txt', 'w')
    ## 파일 읽어오기
    with open(sys.argv[2]) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    fd = []
    for line in lines:
        fd.append(line.split('\t')) #fd[로우][칼럼]

    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    comp = []
    for line in lines:
        if line.find('ms') != -1:
            break
        if line.find('time') != -1:
            break
        comp.append(line.split(' ')) #fd[로우][칼럼]

    r = len(fd)
    c = len(fd[0])
    for i in range(r):
        fd[i] = list(map(float, fd[i]))
    ##
    inputlist = [[] for i in range(len(comp))]  #과제 클러스터링 결과 저장 리스트
    idx = 0
    for i in comp:
        count = 0
        for j in i:
            count += 1
            if (count == 1 and j.find(':') != -1) or (j == ''):
                continue
            inputlist[idx].append(j)
        idx += 1

    P = [[0 for i in range(r)] for i in range(r)]
    C = [[0 for i in range(r)] for i in range(r)]

    for i in inputlist:
        for j in i:
            flag = 0
            for k in i:
                if j == k:
                    flag = 1
                    continue
                if flag == 0:
                    continue
                C[int(j)][int(k)] = 1
                C[int(k)][int(j)] = 1

    k = 10  #클러스터 수
    groundcluster = [[] for i in range(k)]  #ground클러스터 인덱스별 정리
    idx = 0
    for i in fd:
        if int(i[0]) != -1:
            groundcluster[int(i[0]-1)].append(idx)
        idx += 1

    for i in groundcluster:
        for j in i:
            flag = 0
            for k in i:
                if j == k:
                    flag = 1
                    continue
                if flag == 0:
                    continue
                P[int(j)][int(k)] = 1
                P[int(k)][int(j)] = 1

    SS,etc = 0,0
    for i in range(r):
        flag = 0
        for j in range(r):
            if i == j:
                flag = 1
                continue
            if flag == 0:
                continue

            if P[i][j] == 1 and C[i][j] == 1:
                SS += 1
                etc += 1
            elif P[i][j] == 0 and C[i][j] == 0:
                continue
            else:
                etc += 1
    print(str(round((SS/etc)*100, 2)) + '%')
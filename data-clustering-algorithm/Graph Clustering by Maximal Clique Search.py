import sys
import copy

if __name__ == '__main__':
    sys.stdout = open('assignment5_output.txt', 'w')
    ## 파일 읽어오기
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    fd = []
    for line in lines:
        fd.append(line.split('\t')) #fd[로우][칼럼]

    r = len(fd)
    c = len(fd[0])
    ##
    cluster = dict()    #gen id별로 연결된 vertex들
    for i in fd:    #라인
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

    clique = []
    # 3clique 탐색 및 리스트 저장. 주어진 파일이 이미 2clique이므로 3으로 구함.
    for i in cluster:   # cluster[i]. 하나의 vertex에 연결된 vertex 리스트
        if len(cluster[i])>=2:
            for j in cluster[i]:
                flag = 0
                for k in cluster[i]:
                    if j==k:
                        flag = 1
                        continue
                    if flag==0:
                        continue
                    if j in cluster[k]:
                        if [i,j,k] not in clique and [i,k,j] not in clique and [j,i,k] not in clique and [j,k,i] not in clique and [k,i,j] not in clique and [k,j,i] not in clique:
                            clique.append([i,j,k])

    count = 3
    clique_up = []
    clique_result = []
    while True:
        if not clique:
            break
        count += 1

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
                            if count >= 8:

                                ## maximal만 구할 때 이 코드를 사용하고, 전체를 구하려면 주석처리하면 됩니다.
                                result_copy = copy.deepcopy(clique_result)

                                for oneclique in result_copy:
                                    cl_count = 0
                                    for m in oneclique:
                                        if m not in appendlist:
                                            cl_count += 1
                                            break
                                    if cl_count == 0:
                                        clique_result.remove(oneclique)
                                ##
                                clique_result.append(appendlist)

        clique = clique_up.copy()


    clique_result.sort(key=lambda x: len(x), reverse=True)

    for i in clique_result:
        print(str(len(i)) + ':', end=' ')
        for j in i:
            print(j, end=' ')
        print()

    sys.stdout.close()
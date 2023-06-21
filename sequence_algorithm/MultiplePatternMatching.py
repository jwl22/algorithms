# Multiple Pattern Matching를 수행하는 코드이다.(AC 알고리즘)
# python3(WIN: python) MultiplePatternMatching.py test.txt test2.txt 와 같이 사용한다.
# 출력파일: assignment8_output.txt
# 딕셔너리를 이용한 트리 구조이다.
# case-insensitive 하기에 출력은 모두 대문자이다.

import sys
import time
from collections import deque

sys.setrecursionlimit(10000)

input = sys.stdin.readline
result = dict()
tree = [dict(), dict(), False, ""]

if __name__ == '__main__':
    ## 파일 읽어오기
    try:
        with open(sys.argv[1], 'r') as f:
        # with open("test1.txt") as f:
            file1 = f.readlines()
        with open(sys.argv[2], 'r') as f:
        # with open("test2.txt") as f:
            file2 = f.readlines()
    except:
        print("No input file")
        exit()

    ## 파일 로드 및 에러 체크
    if not file1 or not file2:
        print("No string found")  # 빈 파일일 때
        exit()
    elif len(file1) == 1 and len(file2) == 1:
        print("No multiple patterns found")
        exit()
    elif len(file1) > 1 and len(file2) > 1:
        print("No text found")
        exit()
    elif len(file1) > len(file2):
        single_text = file2[0].upper().rstrip()
        multiple_pattern = file1
    else:
        single_text = file1[0].upper().rstrip()
        multiple_pattern = file2

    tic = time.time()
    ## 알고리즘
    # 트리 구성
    for i in multiple_pattern:
        if i != ' ':
            i = i.upper().rstrip()
        result[i] = []
        now = tree
        for j in i:
            if j not in now[0]:
                now[0][j] = [dict(), dict(), False, ""]
            now = now[0][j]
        now[2] = True
        now[3] = i
    tree[1] = tree

    # failure function
    for i in multiple_pattern:
        if i != ' ':
            i = i.upper().rstrip()

        now = tree
        cur_point = tree[0][i[0]]
        cur_point[1] = tree

        for j in i[1:]:
            cur_point = cur_point[0][j]
            if j in now[0]:
                now = now[0][j]
                cur_point[1] = now
            else:
                now = tree
                if j in now[0]:
                    now = now[0][j]
                cur_point[1] = now

    now = tree
    idx = 0
    for i in single_text:
        if i != ' ':
            i = i.upper().rstrip()
        while i not in now[0]:
            now = now[1]
            if now[2] == True:
                result[now[3]].append(idx-len(now[3]))
            if now == tree:
                break
        if i in now[0]:
            now = now[0][i]
            if now[2] == True:
                result[now[3]].append(idx-len(now[3])+1)
        idx += 1
    now = now[1]
    while now[2] == True:
        result[now[3]].append(idx - len(now[3]))
        now = now[1]


    toc = time.time()

    ## 출력
    if not result:
        print('No match found')
        exit()
    result_sum = 0
    for i in multiple_pattern:
        if i != ' ':
            i = i.upper().rstrip()
        result_sum += len(result[i])
    if result_sum == 0:
        print('No match found')
        exit()
    with open('assignment8_output.txt', 'w') as f:
        for i in multiple_pattern:
            if i != ' ':
                i = i.upper().rstrip()
            f.write(i + ': ')
            for j in result[i]:
                f.write(str(j) + ' ')
            f.write('\n')
    elapsed_time = (toc - tic) * 1000000
    print("소요 시간 (use RE): %.3f μs" % elapsed_time)
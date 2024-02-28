# Longest Pattern Finding를 수행하는 코드이다. (anti-monotonic)
# python3(WIN: python) Reverse_Complement.py test.txt 와 같이 사용한다.
# 출력파일: assignment9_output.txt
# 강의시간에 설명해주신대로 DNA Sequence에 포함된 \n 및 띄어쓰기는 제거 후 concat하여 확인한다.
# FASTA는 시작이 >인 문자열로 파악한다.
# case-insensitive하므로 출력은 모두 대문자로 한다.

import re
import sys
import time
from collections import deque

sys.setrecursionlimit(10000)

input = sys.stdin.readline
p = re.compile('[^atcgATCG]')
result_num = 0
result = deque()
DNAsequences = []
impossible = []

def dfs(seq):
    global DNAsequences, result_num, result

    flag = 0
    for i in DNAsequences:
        if seq in i:
            flag += 1
        else:
            break

    if flag == len(DNAsequences):
        if len(seq) > 2 and len(seq) > result_num:
            result_num = len(seq)
            result = [seq]
        elif len(seq) > 2 and len(seq) == result_num and seq not in result:
            result.append(seq)
        # ispossible = [1, 1, 1, 1] # A T C G
        # for k in impossible:
        #     if len(k) > len(seq)+1:
        #         continue
        #     if k in seq + 'A':
        #         ispossible[0] = 0
        #     if k in seq + 'T':
        #         ispossible[1] = 0
        #     if k in seq + 'C':
        #         ispossible[2] = 0
        #     if k in seq + 'G':
        #         ispossible[3] = 0

        tmp = ['A','T','C','G']
        for k in tmp:
            dfs(seq+k)
        # for k in range(len(ispossible)):
        #     if ispossible[k] == 1:
        #         dfs(seq+tmp[k])
    # else:
    #     impossible.append(seq)

if __name__ == '__main__':
    ## 파일 읽어오기
    try:
        # with open('test1.txt') as f:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
    except:
        print("No input file")
        exit()

    ## 파일 체크 및 불러오기
    try:
        line = lines.pop(0)
    except:
        print("No DNA sequence")  # 빈 파일일 때
        exit()

    if line[0] != '>':
        print("No correct format")
        exit()
    linesum = ""
    for line in lines:
        if line[0] == '>':
            DNAsequences.append(linesum)
            linesum = ""
            continue

        line = line.rstrip().replace(' ', '').upper()
        if p.search(line):
            print("No DNA sequence")
            exit()
        linesum += line
    if linesum:
        DNAsequences.append(linesum)
    if len(DNAsequences) == 1:
        print("Need more sequences")
        exit()

    tic = time.time()
    ## 탐색
    dfs("A")
    dfs("T")
    dfs("C")
    dfs("G")

    toc = time.time()
    # 출력
    if result_num == 0:
        print("No pattern found")
        exit()
    with open('assignment9_output.txt', 'w') as f:
        for i in result:
            f.write(i)
            f.write('\n')

    elapsed_time = (toc - tic) * 1000000
    print("소요 시간 (use RE): %.3f μs" % elapsed_time)

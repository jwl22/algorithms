# Longest Common Subsequence를 찾는 코드이다. (dynamic programming)
# python3(WIN: python) LongestCommonSubsequence.py test.txt 와 같이 사용한다.
# 출력파일: assignment4_output.txt
# DNA Sequence에 포함된 \n 및 띄어쓰기는 제거 후 concat하여 확인한다.
# FASTA는 시작이 >인 문자열로 파악한다.
# 백트래킹 시 대각->수평->수직 순서로 탐색하여 파일에 출력한다. 다만 29~36라인 주석 처리 시에만 모두 탐색하며, 주어진 조건 상 하나만 출력한다.

import re
import sys
import time
from collections import deque

input = sys.stdin.readline
p = re.compile('[^atcgATCG]')
result = deque()
score = [[]]
visited = deque()
DNA = ""
first_DNA = ""
second_DNA = ""


def dfs(row, col, seq):
    if row < 0 or col < 0:
        return
    if score[row][col] == 0:
        ## 하나만 탐색한다면. 모두 탐색하려면 36라인 ##까지 주석처리
        with open('assignment4_output.txt', 'w') as f:
            f.write(seq)
            f.write('\n')

        toc = time.time()
        elapsed_time = (toc - tic) * 1000000
        print("소요 시간 (use RE): %.3f μs" % elapsed_time)
        exit()
        ##

        if seq not in result:
            result.append(seq)
        return

    if row - 1 >= 0 and col - 1 >= 0 and first_DNA[row - 1] == second_DNA[col - 1] and [
        row - 1, col - 1, seq] not in visited:
        visited.append([row - 1, col - 1, seq])
        dfs(row - 1, col - 1, first_DNA[row - 1] + seq)
    if col - 1 >= 0 and score[row][col - 1] == score[row][col]:
        dfs(row, col - 1, seq)
    if row - 1 >= 0 and score[row - 1][col] == score[row][col]:
        dfs(row - 1, col, seq)


if __name__ == '__main__':
    ## 파일 읽어오기
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    ## 첫 줄 제거 및 체크
    try:
        line = lines.pop(0)
    except:
        print("No DNA sequence")  # 빈 파일일 때
        exit()

    if line[0] != '>':
        print("No correct format")
        exit()
    # else:
    # result.append(line.rstrip())

    tic = time.time()

    ## 탐색
    for line in lines:
        if line[0] == '>':
            if first_DNA:
                break
            # result.append(line.rstrip())
            first_DNA = DNA
            DNA = ""
            continue

        line = line.rstrip().replace(' ', '')
        if p.search(line):
            print("No DNA sequence")
            exit()
        DNA += line
    second_DNA = DNA
    if not second_DNA:
        print("Need one more sequence")
        exit()

    score = [[0 for _ in range(len(second_DNA) + 1)] for _ in range(len(first_DNA) + 1)]
    for i in range(1, len(first_DNA) + 1):
        for j in range(1, len(second_DNA) + 1):
            if first_DNA[i - 1] == second_DNA[j - 1]:
                score[i][j] = max(score[i - 1][j - 1] + 1, score[i - 1][j], score[i][j - 1])
            else:
                score[i][j] = max(score[i - 1][j], score[i][j - 1])

    dfs(len(first_DNA), len(second_DNA), "")

    # print(result)

    # 출력
    with open('assignment4_output.txt', 'w') as f:
        for i in result:
            f.write(i)
            f.write('\n')

    toc = time.time()
    elapsed_time = (toc - tic) * 1000000
    print("소요 시간 (use RE): %.3f μs" % elapsed_time)

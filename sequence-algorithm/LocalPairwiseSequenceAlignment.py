# Local Pairwise Sequence Alignment를 수행하는 코드이다.
# python3(WIN: python) LocalPairwiseSequenceAlignment.py test.txt 와 같이 사용한다.
# blosum62.txt 파일이 같은 폴더에 있어야 한다.
# 출력파일: assignment5_output.txt
# protein Sequence에 포함된 \n 및 띄어쓰기는 제거 후 concat하여 확인한다.
# FASTA는 시작이 >인 문자열로 파악한다.
# 영문자가 아닌 문자가 단백질 문자열에 포함되어 있으면 No protein sequence를 출력한다.
# 출력 시퀀스의 길이가 60을 넘으면 각각 한 줄 씩 비교할 수 있도록 출력한다. 단 60개 이후 나오는 다음 두 줄은 \n 하나만으로 줄 공백 없이 출력한다.

import re
import sys
import time
from collections import deque

input = sys.stdin.readline
p = re.compile('[^a-zA-Z]')
result = deque()
score = [[]]
blosum62 = dict()
blosum62_file = []
# visited = deque()
protein = ""
first_protein = ""
second_protein = ""
best_score = 0
best_idx = []


def dfs(row, col, seq1, seq2):
    if row < 0 or col < 0:
        return
    if score[row][col] == 0:
        # if seq not in result:
        #     result.append(seq)
        if len(seq1) > 60:
            for j, k in zip(
                    [seq1[i:i + 60] for i in range(0, len(seq1), 60)],
                    [seq2[i:i + 60] for i in range(0, len(seq2), 60)]):
                result.append(j)
                result.append(k)
        else:
            result.append(seq1)
            result.append(seq2)
        # result.append(' ')

        ### 하나만 출력한다면
        toc = time.time()
        with open('assignment5_output.txt', 'w') as f:
            for i in result:
                f.write(i)
                f.write('\n')
        elapsed_time = (toc - tic) * 1000000
        print("소요 시간 (use RE): %.3f μs" % elapsed_time)
        exit()
        ###
        return

    # if row - 1 >= 0 and col - 1 >= 0 and first_protein[row - 1] == second_protein[col - 1] and [
    #     row - 1, col - 1, seq] not in visited:
    if row - 1 >= 0 and col - 1 >= 0 and score[row - 1][col - 1] == (score[row][col] - blosum62[first_protein[row - 1]][
        second_protein[col - 1]]):
        # visited.append([row - 1, col - 1, seq])
        dfs(row - 1, col - 1, first_protein[row - 1] + seq1, second_protein[col - 1] + seq2)
    if col - 1 >= 0 and max(score[row][col - 1] - 5, 0) == score[row][col]:
        dfs(row, col - 1, '-' + seq1, second_protein[col - 1] + seq2)
    if row - 1 >= 0 and max(score[row - 1][col] - 5, 0) == score[row][col]:
        dfs(row - 1, col, first_protein[row - 1] + seq1, '-' + seq2)


if __name__ == '__main__':
    ## 파일 읽어오기
    try:
        with open("blosum62.txt", 'r') as f:
            # with open("test2.txt") as f:
            blosum62_file = f.readlines()
        with open(sys.argv[1], 'r') as f:
            # with open("test.txt") as f:
            lines = f.readlines()
    except:
        print("No input file")
        exit()

    ## 파일 로드 및 에러 체크
    try:
        line = lines.pop(0)
    except:
        print("No protein sequence")  # 빈 파일일 때
        exit()

    if line[0] != '>':
        print("No correct format")
        exit()

    for line in lines:
        if line[0] == '>':
            if first_protein:
                break
            first_protein = protein.upper()
            protein = ""
            continue

        line = line.rstrip().replace(' ', '')
        if p.search(line):
            print("No protein sequence")
            exit()
        protein += line
    if not first_protein:
        print("Need one more sequence")
        exit()
    second_protein = protein.upper()
    if not second_protein:
        print("Need one more sequence(second sequence empty)")
        exit()

    protein_list = blosum62_file.pop(0)
    protein_list = protein_list.rstrip().split('\t')
    protein_list.pop(0)  # 빈 칸 제거
    for i in protein_list:
        blosum62[i.upper()] = dict()
    for line in blosum62_file:
        s = line.rstrip().split('\t')
        i = s.pop(0)
        for j in range(len(protein_list)):
            blosum62[i.upper()][protein_list[j].upper()] = int(s[j])

    tic = time.time()
    ## 탐색
    score = [[0 for _ in range(len(second_protein) + 1)] for _ in range(len(first_protein) + 1)]
    for i in range(1, len(first_protein) + 1):
        for j in range(1, len(second_protein) + 1):
            s1 = first_protein[i - 1].upper()
            s2 = second_protein[j - 1].upper()
            if s1 not in blosum62 and s2 not in blosum62:
                score[i][j] = max(0, score[i - 1][j - 1], score[i - 1][j] - 5, score[i][j - 1] - 5)
            elif s1 not in blosum62 or s2 not in blosum62:
                score[i][j] = max(0, score[i - 1][j - 1] - 5, score[i - 1][j] - 5, score[i][j - 1] - 5)
            else:
                score[i][j] = max(0, score[i - 1][j - 1] + blosum62[s1][s2], score[i - 1][j] - 5, score[i][j - 1] - 5)
            if score[i][j] > best_score:
                best_score = score[i][j]
                best_idx = [[i, j]]
            elif score[i][j] == best_score:
                best_idx.append([i, j])

    result.append(str(best_score))
    if best_score != 0:
        for i in best_idx:
            dfs(i[0], i[1], "", "")

    toc = time.time()
    ## 출력
    with open('assignment5_output.txt', 'w') as f:
        for i in result:
            f.write(i)
            f.write('\n')
    elapsed_time = (toc - tic) * 1000000
    print("소요 시간 (use RE): %.3f μs" % elapsed_time)

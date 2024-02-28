# Multiple Sequence Alignment를 수행하는 코드이다.
# implement multiple sequence alignment using a heuristic algorithm
# pairwise alignments against a center sequence
# python3(WIN: python) MultipleSequenceAlignment.py test.txt 와 같이 사용한다.
# blosum62.txt 파일이 같은 폴더에 있어야 한다.
# 출력파일: assignment6_output.txt
# protein Sequence에 포함된 \n 및 띄어쓰기는 제거 후 concat하여 확인한다.
# FASTA는 시작이 >인 문자열로 파악한다.
# 영문자가 아닌 문자가 단백질 문자열에 포함되어 있으면 No protein sequence를 출력한다.

import re
import sys
import time
from collections import deque

sys.setrecursionlimit(10000)

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
proteins = []
pairwise_score = []
pairwise_score_max = 0
pairwise_score_maxidx = -1
pairwise_seq = []

gap = -5


def ga(seq_idx):
    global score, first_protein, second_protein, pairwise_score, pairwise_score_max, pairwise_score_maxidx

    for i in range(len(proteins)):
        first_protein = proteins[seq_idx]
        second_protein = proteins[i]

        if i == seq_idx:
            continue
        score = [[0 for _ in range(len(second_protein) + 1)] for _ in range(len(first_protein) + 1)]
        for j in range(len(score[0])):
            score[0][j] = gap * j
        for j in range(len(score)):
            score[j][0] = gap * j

        for j in range(1, len(first_protein) + 1):
            for k in range(1, len(second_protein) + 1):
                s1 = first_protein[j - 1].upper()
                s2 = second_protein[k - 1].upper()
                if s1 not in blosum62 and s2 not in blosum62:
                    score[j][k] = max(score[j - 1][k - 1], score[j - 1][k] + gap, score[j][k - 1] + gap)
                elif s1 not in blosum62 or s2 not in blosum62:
                    score[j][k] = max(score[j - 1][k - 1] + gap, score[j - 1][k] + gap, score[j][k - 1] + gap)
                else:
                    score[j][k] = max(score[j - 1][k - 1] + blosum62[s1][s2], score[j - 1][k] + gap,
                                      score[j][k - 1] + gap)

        pairwise_score[seq_idx] += score[len(first_protein)][len(second_protein)]
        pairwise_seq[seq_idx][i][0], pairwise_seq[seq_idx][i][1] = scan(len(first_protein), len(second_protein), "", "")

    if pairwise_score_max < pairwise_score[seq_idx]:
        pairwise_score_max = pairwise_score[seq_idx]
        pairwise_score_maxidx = seq_idx

def scan(row,col,seq1,seq2):
    global first_protein, second_protein

    cur_row = row
    cur_col = col
    while not (cur_row == 0 and cur_col == 0):
        if cur_row - 1 >= 0 and cur_col - 1 >= 0 and score[cur_row - 1][cur_col - 1] == (score[cur_row][cur_col] - blosum62[first_protein[cur_row - 1]][second_protein[cur_col - 1]]):
            seq1 = first_protein[cur_row - 1] + seq1
            seq2 = second_protein[cur_col - 1] + seq2
            cur_row -= 1
            cur_col -= 1
            continue
        if cur_col - 1 >= 0 and score[cur_row][cur_col - 1] + gap == score[cur_row][cur_col]:
            seq1 = '-' + seq1
            seq2 = second_protein[cur_col - 1] + seq2
            cur_col -= 1
            continue
        if cur_row - 1 >= 0 and score[cur_row - 1][cur_col] + gap == score[cur_row][cur_col]:
            seq1 = first_protein[cur_row - 1] + seq1
            seq2 = '-' + seq2
            cur_row -= 1
    return seq1, seq2
# def dfs(row, col, seq1, seq2):
#     if row == 0 and col == 0:
#         tmp.append(seq1)
#         tmp.append(seq2)
#         # if len(seq1) > 60:
#             # for j, k in zip(
#             #         [seq1[i:i + 60] for i in range(0, len(seq1), 60)],
#             #         [seq2[i:i + 60] for i in range(0, len(seq2), 60)]):
#             #     tmp.append(j)
#             #     tmp.append(k)
#         # else:
#         #     tmp.append(seq1)
#         #     tmp.append(seq2)
#         return
#
#     # if row - 1 >= 0 and col - 1 >= 0 and first_protein[row - 1] == second_protein[col - 1] and [
#     #     row - 1, col - 1, seq] not in visited:
#     if row - 1 >= 0 and col - 1 >= 0 and score[row - 1][col - 1] == (score[row][col] - blosum62[first_protein[row - 1]][
#         second_protein[col - 1]]):
#         # visited.append([row - 1, col - 1, seq])
#         dfs(row - 1, col - 1, first_protein[row - 1] + seq1, second_protein[col - 1] + seq2)
#     if col - 1 >= 0 and max(score[row][col - 1] + gap, 0) == score[row][col]:
#         dfs(row, col - 1, '-' + seq1, second_protein[col - 1] + seq2)
#     if row - 1 >= 0 and max(score[row - 1][col] + gap, 0) == score[row][col]:
#         dfs(row - 1, col, first_protein[row - 1] + seq1, '-' + seq2)


if __name__ == '__main__':
    ## 파일 읽어오기
    try:
        with open("blosum62.txt", 'r') as f:
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
        print("No protein sequences")  # 빈 파일일 때
        exit()

    if line[0] != '>':
        print("No correct format")
        exit()

    for line in lines:
        if line[0] == '>':
            proteins.append(protein.upper())
            protein = ""
            continue

        line = line.rstrip().replace(' ', '')
        if p.search(line):
            print("No protein sequences")
            exit()
        protein += line
    if protein:
        proteins.append(protein.upper())
    if len(proteins) == 1:
        print("Need more sequences")
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
    pairwise_score_max = -sys.maxsize * 2 + 1

    tic = time.time()
    ## 탐색
    pairwise_score = [0 for _ in range(len(proteins))]
    pairwise_seq = [[["", ""] for _ in range(len(proteins))] for _ in range(len(proteins))]
    for i in range(len(proteins)):
        ga(i)

    center = pairwise_seq[pairwise_score_maxidx]
    for i in range(len(center)):
        if not center[i][0]:
            continue
        if not result:
            result.append(center[i][0])
            result.append(center[i][1])
            continue

        j = 0
        while True:
            if j >= len(center[i][0]) or j >= len(result[0]):
                result.append(center[i][1])
                break

            if center[i][0][j] != '-' and result[0][j] == '-':
                center[i][0] = center[i][0][:j - 1] + '-' + center[i][0][j - 1:]
                center[i][1] = center[i][1][:j - 1] + '-' + center[i][1][j - 1:]
            elif center[i][0][j] == '-' and result[0][j] != '-':
                for k in range(len(result)):
                    result[k] = result[k][:j] + '-' + result[k][j:]
            j += 1

    cmp_str = ""
    sl_count = len(result[0]) // 60 + 1
    for i in range(len(result[0])):
        cmp = result[0][i]
        flag = 0
        for j in range(1,len(result)):
            if result[j][i] != cmp:
                cmp_str += " "
                flag = 1
                break
        if flag == 0:
            cmp_str += "*"
    result.append(cmp_str)

    tmp = []
    if len(result[0]) > 60:
        for rs in result:
            for j in [rs[i:i + 60] for i in range(0, len(rs), 60)]:
                tmp.append(j)
        result = []
        for j in range(sl_count):
            for i in range(0,len(tmp),sl_count):
                result.append(tmp[i + j])

    result[0] = f"{pairwise_score_maxidx+1}:\t{result[0]}"
    idx = 1
    for i in range(1, len(proteins)):
        if i == pairwise_score_maxidx + 1:
            idx += 1
        result[i] = f"{idx}:\t{result[i]}"
        idx += 1
    for i in range(len(proteins), len(result)):
        result[i] = f"\t{result[i]}"

    # for i in range(1+sl_count, len(result)-1, sl_count):
    #     if i <= pairwise_score_maxidx:
    #         result[i] = f"{i}:\t{result[i]}"
    #     elif i == pairwise_score_maxidx:
    #         continue
    #     else:
    #         result[i] = f"{i+1}:\t{result[i]}"



    toc = time.time()
    ## 출력
    with open('assignment6_output.txt', 'w') as f:
        for i in result:
            f.write(i)
            f.write('\n')
    elapsed_time = (toc - tic) * 1000000
    print("소요 시간 (use RE): %.3f μs" % elapsed_time)

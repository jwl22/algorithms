# FASTA 포멧의 DNA sequence 파일을 읽어오면, 단백질의 Low complexity regions를 출력한다.
# RE 라이브러리를 사용하지 않은 코드이다.
# python3(WIN: python) LowComplexityRegions.py test.txt 와 같이 사용한다.
# 출력파일: assignment3-2_output.txt
# DNA sequence가 아닐 시 터미널에 No DNA sequence 문구를 띄운다.
# 문자열에 포함된 \n 및 띄어쓰기는 제거 후 concat하여 확인한다. 출력 파일에 나오는 인덱스값도 띄어쓰기 제거 후 나온 결과이다.
# FASTA는 시작이 >인 문자열로 파악한다.

import sys
import time
from collections import deque

tic = time.time()

input = sys.stdin.readline

if __name__ == '__main__':
    result = deque()

    ## 파일 읽어오기
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    ## 첫 줄 제거 및 체크
    try:
        line = lines.pop(0)
    except:
        print("No DNA sequence") # 빈 파일일 때
        exit()

    if line[0] != '>':
        print("No correct format")
        exit()
    else:
        result.append(line.rstrip())

    ## 탐색
    DNA = ""
    DNA_scan_str = ["","","",""]
    DNA_scan_match = ["","","",""]
    DNA_scan_match_count = [0,0,0,0]
    for line in lines:
        if line[0] == '>':
            break

        line = line.rstrip().replace(' ', '')
        for i in line:
            if i != 'a' and i != 't' and i != 'c' and i != 'g' and i != 'A' and i != 'T' and i != 'C' and i != 'G':
                print("No DNA sequence")
                exit()
        DNA += line

    idx = 0
    found = []
    tmp = ""
    prev_seq = ""
    len2_chk = 0
    len2_is_same = False
    for i in DNA:
        if prev_seq:
            if i.casefold() != prev_seq[len(tmp)].casefold():
                tmp = ""
                prev_seq = ""
                len2_chk = 0
                len2_is_same = False
            else:
                tmp += i
                if len(prev_seq) == 2 and len2_chk == 0:
                    len2_chk = 6
                    if prev_seq[0].casefold() == prev_seq[1].casefold():
                        len2_is_same = True
                if i.casefold() == prev_seq[0].casefold() and len2_chk != 0 and len2_is_same:
                    len2_chk += 1
                    if len2_chk == 9 or len2_chk == 12 or len2_chk == 15:
                        prev_seq += prev_seq[0]
                        DNA_scan_match = ["", "", "", ""]
                        DNA_scan_match_count = [0, 0, 0, 0]
                        DNA_scan_str = ["", "", "", ""]
                        tmp = ""
                        idx += 1
                        continue
                if len(tmp) == len(prev_seq):
                    if prev_seq.casefold() == tmp.casefold():
                        if len2_chk != 0 and not len2_is_same:
                            len2_chk += 2
                            if len2_chk == 12:
                                prev_seq += prev_seq
                        DNA_scan_match = ["", "", "", ""]
                        DNA_scan_match_count = [0, 0, 0, 0]
                        DNA_scan_str = ["", "", "", ""]
                        tmp = ""
                        idx += 1
                        continue

        length = 2
        for j in range(4):
            if len(DNA_scan_str[j]) == length:
                if DNA_scan_str[j][len(DNA_scan_match[j])].casefold() == i.casefold():
                    DNA_scan_match[j] = DNA_scan_match[j] + i
                    if len(DNA_scan_match[j]) == length:
                        DNA_scan_match_count[j] += 1
                        if DNA_scan_match_count[j] >= 2:
                            prev_seq = DNA_scan_match[j]
                            found.append(idx - (DNA_scan_match_count[j]+1)*length + 1)
                            DNA_scan_match = ["", "", "", ""]
                            DNA_scan_match_count = [0, 0, 0, 0]
                            DNA_scan_str = ["", "", "", ""]
                            break
                        DNA_scan_match[j] = ""
                else:
                    DNA_scan_str[j] = DNA_scan_str[j][len(DNA_scan_match[j])+1:] + DNA_scan_match[j] + i
                    DNA_scan_match_count[j] = 0
                    DNA_scan_match[j] = ""
            else:
                DNA_scan_str[j] += i
            length += 1
        idx += 1
    if not found:
        print("No low-complexity region found")
        exit()
    result.append(found)

    ## 출력
    with open('assignment3-2_output.txt', 'w') as f:
        while result:
            f.write(result.popleft())
            DNAidx = result.popleft()
            for i in DNAidx:
                f.write('\n')
                f.write(str(i))

    toc = time.time()
    elapsed_time = (toc - tic) * 1000000
    print("소요 시간 (not use RE): %.3f μs" % elapsed_time)
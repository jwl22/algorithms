# FASTA 포멧의 DNA sequence 파일을 읽어오면, 단백질의 Low complexity regions를 출력한다.
# RE 라이브러리를 사용한 코드이다.
# python3(WIN: python) LowComplexityRegions_RE.py test.txt 와 같이 사용한다.
# 출력파일: assignment3-1_output.txt
# DNA sequence가 아닐 시 터미널에 No DNA sequence 문구를 띄운다.
# 문자열에 포함된 \n 및 띄어쓰기는 제거 후 concat하여 확인한다. 출력 파일에 나오는 인덱스값도 띄어쓰기 제거 후 나온 결과이다.
# FASTA는 시작이 >인 문자열로 파악한다.

import sys
import re
import time
from collections import deque

tic = time.time()

input = sys.stdin.readline
p = re.compile('[^atcgATCG]')
s = re.compile(r'([ATCG]{2,5})(\1){2,}', re.IGNORECASE)

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
    for line in lines:
        if line[0] == '>':
            break

        line = line.rstrip().replace(' ', '')
        if p.search(line):
            print("No DNA sequence")
            exit()
        DNA += line

    matches_iter = re.finditer(s, DNA)
    tmp = []
    for i in matches_iter:
        tmp.append(i.start())
    if not tmp:
        print("No low-complexity region found")
        exit()
    result.append(tmp)

    ## 출력
    with open('assignment3-1_output.txt', 'w') as f:
        while result:
            f.write(result.popleft())
            DNAidx = result.popleft()
            for i in DNAidx:
                f.write('\n')
                f.write(str(i))

    toc = time.time()
    elapsed_time = (toc - tic) * 1000000
    print("소요 시간 (use RE): %.3f μs" % elapsed_time)
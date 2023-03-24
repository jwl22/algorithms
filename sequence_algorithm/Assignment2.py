# 2018253082 이정우
# python3(WIN: python) Assignment2.py test.txt 와 같이 사용한다.
# 출력파일: assignment2_output.txt
# DNA sequence가 아닐 시 터미널에 No DNA sequence 문구를 띄운다.
# 띄어쓰기(공백)와 개행은 무시하고 concat하여 한 줄로 출력한다.

import sys
import re

input = sys.stdin.readline
p = re.compile('[^atcgATCG]')

old_str = "atcgATCG"
new_str = "tagcTAGC"

if __name__ == '__main__':
    result = ""

    ## 파일 읽어오기
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    ## 첫 줄 제거
    first_line = lines.pop(0)

    ## 변환
    DNA = ""
    for line in lines:
        line = line.rstrip().replace(' ', '')
        if p.search(line):
            print("No DNA sequence")
            exit()
        DNA += line

    DNA_reversed = list(reversed(DNA))
    for i in range(len(DNA_reversed)):
        DNA_reversed[i] = new_str[old_str.index(DNA_reversed[i])]
    DNA_reversed = "".join(DNA_reversed)

    ## 출력
    with open('assignment2_output.txt', 'w') as f:
        f.write(first_line)
        f.write(DNA_reversed)
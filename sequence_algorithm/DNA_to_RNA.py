# DNA시퀀스를 RNA시퀀스로 바꾸는 코드이다.
# python3(WIN: python) DNA _to_RNA.py test.txt 와 같이 사용한다.
# 출력파일: assignment1_output.txt
# DNA sequence가 아닐 시 터미널에 No DNA sequence 문구를 띄운다.
# 띄어쓰기(공백)와 개행은 무시하고 concat하여 한 줄로 출력한다.

import sys
import re

input = sys.stdin.readline
p = re.compile('[^atcgATCG ]')

if __name__ == '__main__':
    result = ""

    ## 파일 읽어오기
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    ## 첫 줄 제거
    tmp = lines.pop(0)

    ## RNA 변환
    for line in lines:
        line = line.rstrip()
        if p.search(line):
            print("No DNA sequence")
            exit()
        line_list = list(line)
        for i in range(len(line_list)):
            if line_list[i] == 'T':
                line_list[i] = 'U'
            elif line_list[i] == 't':
                line_list[i] = 'u'
            elif line_list[i] == ' ':
                line_list[i] = ''
        result += ''.join(line_list)

    with open('assignment1_output.txt', 'w') as f:
        f.write(tmp)
        f.write(result)
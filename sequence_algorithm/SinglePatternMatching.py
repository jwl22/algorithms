# Single Pattern Matching를 수행하는 코드이다. (KMP Algorithm)
# python3(WIN: python) SinglePatternMatching.py test.txt test2.txt 와 같이 사용한다.
# 출력파일: assignment7_output.txt
# 파일 속에 개행이 있으면 그 전까지만 string으로 파악한다.

import sys
import time
from collections import deque

sys.setrecursionlimit(10000)

input = sys.stdin.readline
result = deque()

if __name__ == '__main__':
    ## 파일 읽어오기
    try:
        with open(sys.argv[1], 'r') as f:
        # with open("test1.txt") as f:
            file1 = f.readline().upper().rstrip()
        with open(sys.argv[2], 'r') as f:
        # with open("test2.txt") as f:
            file2 = f.readline().upper().rstrip()
    except:
        print("No input file")
        exit()

    ## 파일 로드 및 에러 체크
    if not file1 or not file2:
        print("No string found")  # 빈 파일일 때
        exit()
    if len(file1) > len(file2):
        short_str = file2
        long_str = file1
    else:
        short_str = file1
        long_str = file2

    
    tic = time.time()
    ## 알고리즘
    P = [0 for _ in range(len(short_str))]
    tmp = 0
    for i in range(1, len(short_str)):
        if short_str[tmp] == short_str[i]:
            tmp += 1
        else:
            tmp = 0
        P[i] = tmp

    jump = 0
    for i in range(len(long_str)):
        if len(short_str) + i > len(long_str):
            break
        if jump > 0:
            jump -= 1
            continue

        same_count = 0
        for j in short_str:
            if long_str[i+same_count] == j:
                same_count += 1
                if same_count == len(short_str):
                    result.append(i)
            else:
                jump = same_count - P[same_count-1] - 1
                break

    toc = time.time()

    ## 출력
    if not result:
        print('No match found')
        exit()
    with open('assignment7_output.txt', 'w') as f:
        for i in result:
            f.write(str(i)+' ')
    elapsed_time = (toc - tic) * 1000000
    print("소요 시간 (use RE): %.3f μs" % elapsed_time)
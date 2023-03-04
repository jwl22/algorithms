import sys

input = sys.stdin.readline

line = input().rstrip()
i = 1
while True:
    str_i = str(i)
    while line[0] in str_i:
        str_i = str_i[str_i.index(line[0]) + 1:]
        line = line[1:]
        if not line:
            print(i)
            exit()
    i += 1

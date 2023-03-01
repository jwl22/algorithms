import sys

input = sys.stdin.readline

# N이하의 수, K=자릿수, P=반전시킬 최대 LED갯수, X=실제 층 수
N, K, P, X = map(int, input().rstrip().split())

el_num = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0],
          [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]

N_str = str(N)
X_str = str(X)
# while len(X_str) != len(N_str):
#     X_str = '0' + X_str
X_str = X_str.zfill(len(N_str))

result = 0
for i in range(1, N + 1):
    count = 0
    i_str = str(i)
    # while len(i_str) != len(N_str):
    #     i_str = '0' + i_str
    i_str = i_str.zfill(len(N_str))
    for j in range(len(N_str)):
        if X_str[j] != i_str[j]:
            X_str_int = int(X_str[j])
            i_str_int = int(i_str[j])
            for k in range(7):
                if el_num[X_str_int][k] != el_num[i_str_int][k]:
                    count += 1
                if count > P:
                    break
    if count <= P and count != 0:
        result += 1

print(result)

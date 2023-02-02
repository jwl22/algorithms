import sys
input = sys.stdin.readline

N = int(input())
N_len = len(str(N))

result = 0

while N_len>1:
    result += ((10**(N_len-1)) - (10**(N_len-2))) * (N_len-1)
    N_len -= 1

N_len = len(str(N))
result += ((N//(10**(N_len-1))) - 1) * N_len * 10**(N_len-1)
result += (N%(10**(N_len-1)) + 1) * N_len

print(result)
import sys

input = sys.stdin.readline

N = int(input())
users = []
for _ in range(N):
    users.append(list(input().rstrip().split()))
users = sorted(users, key=lambda x: int(x[0]))
for i in users:
    print(i[0], i[1])

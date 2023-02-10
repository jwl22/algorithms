import sys
input = sys.stdin.readline

N = int(input())
T,P = [], []
for _ in range(N):
    t,p = map(int,input().rstrip().split())
    T.append(t)
    P.append(p)
best = 0

def func1(day, income):
    global N, best
    if day>=N or T[day]+day > N:
        if best<income:
            best = income
        return
    income += P[day]
    for i in range(day+T[day],N):
        func1(i, income)
    if best<income:
        best = income
    return

for i in range(N):
    func1(i, 0)

print(best)
import sys
input = sys.stdin.readline

K, L = map(int, input().split())

registration_complete = {}  # 수강신청에 성공한 학번
for i in range(L):
    student_id = input()
    registration_complete[student_id] = i

registration_complete_sorted = sorted(
    registration_complete.items(), key=lambda x: x[1])

count = 0
for student_id, _ in registration_complete_sorted:
    if count+1 > K:
        break
    print(student_id, end='')
    count += 1

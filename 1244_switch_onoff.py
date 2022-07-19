from operator import index
import sys
input = sys.stdin.readline

switch_count = int(input())  # 스위치 개수
count_list = map(int, input().split())  # 스위치의 상태
arr_list = []  # 스위치 상태의 리스트
for i in count_list:
    arr_list.append(i)

student_count = int(input())  # 학생 수

for _ in range(0, student_count):
    gender, number = map(int, input().split())
    if gender == 1:
        index_number = number
        while index_number-1 < len(arr_list):
            if arr_list[index_number-1] == 0:
                arr_list[index_number-1] = 1
            else:
                arr_list[index_number-1] = 0
            index_number += number
    elif gender == 2:
        if arr_list[number-1] == 0:
            arr_list[number-1] = 1
        else:
            arr_list[number-1] = 0
        num = 1
        while number-num-1 >= 0 and number+num-1 < len(arr_list) and arr_list[number-num-1] == arr_list[number+num-1]:
            if arr_list[number-num-1] == 0:
                arr_list[number-num-1] = 1
            else:
                arr_list[number-num-1] = 0
            if arr_list[number+num-1] == 0:
                arr_list[number+num-1] = 1
            else:
                arr_list[number+num-1] = 0
            num += 1
    else:
        continue

count = 1
for i in arr_list:
    if count != 0 and count % 20 == 0:
        print(i)
    else:
        print(i, end=" ")
    count += 1

from collections import deque
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    sorted_stack = deque(range(1, n+1))
    index = past_index = 0

    answer = deque()

    try:
        for i in range(n):
            find_num = int(input())
            if i == 0 or past_index == index == 0:
                answer.append('+')
            while sorted_stack[index] != find_num:
                index += 1
                answer.append('+')

            past_index = index
            sorted_stack.rotate(-index)
            sorted_stack.popleft()
            sorted_stack.rotate(index)
            if index >= 1:
                index -= 1
            answer.append('-')

        print('\n'.join(answer))
    except:
        print('NO')


sol()

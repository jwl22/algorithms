import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

# def add(string, s, is_reverse):
#     global T

#     if s == 'A':
#         if is_reverse == 0:
#             string += s
#         else:
#             string = 'A' + string
#     else:
#         if is_reverse == 0:
#             string += s
#             is_reverse = 1
#         else:
#             string = 'B' + string
#             is_reverse = 0

#     if len(string) == len(T):
#         if is_reverse == 1:
#             string = list(string)
#             string.reverse()
#             string = ''.join(string)
#         if string == T:
#             print(1)
#             exit()
#         else:
#             return
#     AorB(string, is_reverse)


def delete(string, p):
    global S

    if p == 0:
        string = string[1:]
        string = list(string)
        string.reverse()
        string = ''.join(string)
    else:
        string = string[:-1]

    if len(string) == len(S):
        if string == S:
            print(1)
            exit()
        else:
            return
    AorB(string)


def AorB(string):
    if string[0] == 'B':
        delete(string, 0)
    if string[-1] == 'A':
        delete(string, -1)


AorB(T)
print(0)

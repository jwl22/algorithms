import sys
input = sys.stdin.readline

variableName = input()
variableName = variableName.replace("\n", "")
arr = []

isJava = -1  # 0:C++ 1:JAVA

for i in variableName:
    arr.append(i)

result = ""
isNext = 0
for i in arr:
    if i.isupper() == 1:
        if isJava == 0 or result == "":
            result = "Error!"
            break
        isJava = 1
        result += '_' + i.lower()
        continue
    elif isNext == 1:
        if i == '_':
            result = "Error!"
            break
        result += i.upper()
        isNext = 0
        continue
    elif i == "_":
        if isJava == 1 or result == "":
            result = "Error!"
            break
        isJava = 0
        isNext = 1
        continue

    result += i

if result == "" or isNext == 1:
    result = "Error!"

print(result)

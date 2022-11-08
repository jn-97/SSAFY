import sys

sys.stdin = open("2019.txt")

n = int(input())

result = [1]

i = 1
while True:
    i = i * 2
    result.append(i)
    if len(result) == n + 1:
        print(*result, end=" ")
        break

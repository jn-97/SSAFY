import sys

sys.stdin = open("1933.txt")

n = int(input())

result = []
for i in range(1, n + 1):
    if n % i == 0:
        result.append(i)
    else:
        pass
print(*result, end=" ")

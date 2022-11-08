import sys

sys.stdin = open("2046.txt")

n = int(input())

result = []
for i in range(n):
    result.append("#")
print(*result, sep="")

import sys

sys.stdin = open("1545.txt")

n = int(input())

for i in range(0, n + 1):
    print(n - i, end=" ")

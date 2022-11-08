import sys

sys.stdin = open("2043.txt")

P, K = map(int, input().split())

if P > K:
    print((P - K) + 1)
elif P == K:
    print(0)
else:
    print((K - P) + 1)

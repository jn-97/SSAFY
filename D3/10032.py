import sys, math

sys.stdin = open("10032.txt")

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())

    a = n // k
    b = n % k
    if b > 0:
        print(f"#{tc} {a - b}")
    else:
        print(f"#{tc} 0")

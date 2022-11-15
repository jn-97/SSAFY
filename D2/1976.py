import sys
import math

sys.stdin = open("1976.txt")

T = int(input())

for tc in range(1, T + 1):
    H, M, h, m = map(int, input().split())

    sum_ = ((H + h) * 60) + (M + m)

    Hh = math.trunc(sum_ / 60)
    Mm = sum_ % 60

    if Hh > 12:
        Hh -= 12
    print(f"#{tc} {Hh} {Mm}")

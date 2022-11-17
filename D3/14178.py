import math

T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())

    if a % ((b * 2) + 1) != 0:
        print(f"#{tc} {math.trunc(a/((b*2)+1)+1)}")
    else:
        print(f"#{tc} {math.trunc(a/((b*2)+1))}")

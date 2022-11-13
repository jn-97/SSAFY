import sys
from pprint import pprint

sys.stdin = open("1983.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    list_ = []
    for _ in range(N):
        list_.append(list(map(int, input().split())))

    result = []
    for i in range(N):
        result.append(
            (list_[i][0]) * 0.35 + (list_[i][1] * 0.45 + (list_[i][2] * 0.20))
        )

    cnt = 0
    for j in range(N):
        if result[j] > result[K - 1]:
            cnt += 1
    if cnt == 0:
        print(f"#{tc} A+")
    elif cnt == 1:
        print(f"#{tc} A0")
    elif cnt == 2:
        print(f"#{tc} A-")
    elif cnt == 3:
        print(f"#{tc} B+")
    elif cnt == 4:
        print(f"#{tc} B0")
    elif cnt == 5:
        print(f"#{tc} B-")
    elif cnt == 6:
        print(f"#{tc} C+")
    elif cnt == 7:
        print(f"#{tc} C0")
    elif cnt == 8:
        print(f"#{tc} C-")
    else:
        print(f"#{tc} D0")

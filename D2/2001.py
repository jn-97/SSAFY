import sys
from pprint import pprint

sys.stdin = open("2001.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    list_ = []
    for _ in range(N):
        list_.append(list(map(int, input().split())))

    temp = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp2 = 0
            for k in range(M):
                for l in range(M):
                    temp2 += list_[i + k][j + l]
                    if temp < temp2:
                        temp = temp2

    print(f"#{tc} {temp}")

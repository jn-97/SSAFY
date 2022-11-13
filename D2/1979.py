import sys
from pprint import pprint

sys.stdin = open("1979.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    list_ = []
    for _ in range(N):
        list_.append(list(map(int, input().split())))

    cnt1 = 0
    result1 = 0
    for i in range(N):
        for j in range(N):
            if list_[i][j] == 1:
                cnt1 += 1
            else:
                if cnt1 == K:
                    result1 += 1
                    cnt1 = 0
                else:
                    cnt1 = 0
        if cnt1 == K:
            result1 += 1
            cnt1 = 0
        else:
            cnt1 = 0

    cnt2 = 0
    result2 = 0
    for i in range(N):
        for j in range(N):
            if list_[j][i] == 1:
                cnt2 += 1
            else:
                if cnt2 == K:
                    result2 += 1
                    cnt2 = 0
                else:
                    cnt2 = 0
        if cnt2 == K:
            result2 += 1
            cnt2 = 0
        else:
            cnt2 = 0

    print(f"#{tc} {result1 + result2}")

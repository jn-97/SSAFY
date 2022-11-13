import sys

sys.stdin = open("1859.txt")


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    list_ = list(map(int, input().split()))

    list_ = list_[::-1]
    result = 0
    temp_ = list_[0]

    for i in range(1, n):
        if temp_ > list_[i]:
            result += temp_ - list_[i]
        else:
            temp_ = list_[i]
    print(f"#{tc} {result}")

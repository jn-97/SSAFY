import sys

sys.stdin = open("13038.txt")

# 100개 중 82개
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    list_ = list(map(int, input().split()))

    list_.insert(0, list_[6])
    list_.pop()

    days = 0
    i = 0
    while True:
        if list_[i] == 1:
            days += 1
            n -= 1
            if n == 0:
                print(f"#{tc} {days}")
                break
            elif n != 0:
                if i == 6:
                    i = 0
                else:
                    i += 1
        else:
            if days > 0:
                days += 1
            if n != 0:
                if i == 6:
                    i = 0
                else:
                    i += 1

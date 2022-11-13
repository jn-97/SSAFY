import sys

sys.stdin = open("1984.txt")

T = int(input())

for tc in range(1, T + 1):
    list_ = list(map(int, input().split()))

    list_.remove(max(list_))
    list_.remove(min(list_))

    print(f"#{tc} {round(sum(list_) / 8)}")

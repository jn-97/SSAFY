import sys

sys.stdin = open("2071.txt")

T = int(input())

for tc in range(1, T + 1):
    list_ = list(map(int, input().split()))

    print(f"#{tc} {round(sum(list_) / 10)}")

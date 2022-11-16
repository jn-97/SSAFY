import sys

sys.stdin = open("1966.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    list_ = list(map(int, input().split()))
    list_ = sorted(list_)

    print(f"#{tc}", *list_)

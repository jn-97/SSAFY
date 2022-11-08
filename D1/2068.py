import sys

sys.stdin = open("2068.txt")

T = int(input())

for tc in range(1, T + 1):
    list_ = list(map(int, input().split()))
    print(f"#{tc} {max(list_)}")

import sys

sys.stdin = open("2072.txt")

T = int(input())

for tc in range(1, T + 1):
    list_ = list(map(int, input().split()))

    result = 0
    for i in range(len(list_)):
        if list_[i] % 2 != 0:
            result += list_[i]

    print(f"#{tc} {result}")

import sys

sys.stdin = open("1970.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    list_ = []
    list_.append(n // 50000)
    n = n % 50000
    list_.append(n // 10000)
    n = n % 10000
    list_.append(n // 5000)
    n = n % 5000
    list_.append(n // 1000)
    n = n % 1000
    list_.append(n // 500)
    n = n % 500
    list_.append(n // 100)
    n = n % 100
    list_.append(n // 50)
    n = n % 50
    list_.append(n // 10)
    n = n % 10
    print(f"#{tc}")
    print(*list_)

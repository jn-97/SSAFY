import sys

sys.stdin = open("2056.txt")

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for tc in range(1, T + 1):
    date = input()
    month = int(date[4:6])
    day = int(date[6:8])

    result = "-1"

    if 1 <= month and month <= 12 and 1 <= day and day <= date[month]:
        result = date[0:4] + "/" + date[4:6] + "/" + date[6:8]
    print(f"#{tc} {result}")

# 런타임 에러

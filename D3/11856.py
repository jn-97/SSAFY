import sys

sys.stdin = open("11856.txt")

T = int(input())

for tc in range(1, T + 1):
    S = input()

    if len(set(list(S))) == 2:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")

    print(set(S))

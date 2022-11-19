import sys

sys.stdin = open("14361.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    for i in range(2, 11):
        N = n * i

        if len(str(n)) == len(str(N)):
            s_n = sorted(str(n))
            s_N = sorted(str(N))
            if s_n == s_N:
                print(f"#{tc} possible")
                break
            else:
                continue
        else:
            print(f"#{tc} impossible")
            break

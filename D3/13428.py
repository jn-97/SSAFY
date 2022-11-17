import sys

sys.stdin = open("13428.txt")

T = int(input())

for tc in range(1, T + 1):
    n = list(input())
    min_n, max_n = "".join(n), "".join(n)

    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if i == 0 and n[j] == "0":
                continue

            n[i], n[j] = n[j], n[i]
            min_n = min(min_n, "".join(n))
            max_n = max(max_n, "".join(n))
            n[i], n[j] = n[j], n[i]

    print(f"#{tc} {min_n} {max_n}")

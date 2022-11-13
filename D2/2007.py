import sys

sys.stdin = open("2007.txt")

T = int(input())

words = []
for tc in range(1, T + 1):
    words = list(map(str, input().split()))
    print(words)
    for i in range(1, 11):
        if words[0][0 : i + 1] == words[0][i + 1 : 2 * (i + 1)]:
            print(f"#{tc} {i+1}")
            break

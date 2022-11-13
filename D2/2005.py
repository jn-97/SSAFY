import sys

sys.stdin = open("2005.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    result = [[1]]

    for i in range(1, n):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(temp)

    print(f"#{tc}")
    for line in result:
        print(*line)

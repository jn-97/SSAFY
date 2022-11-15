T = int(input())


def check(arr):
    for i in range(9):
        row = []
        for j in range(9):
            if row:
                if arr[i][j] in row:
                    return 0
            row.append(arr[i][j])

    for i in range(9):
        column = []
        for j in range(9):
            if column:
                if arr[j][i] in column:
                    return 0
            column.append(arr[j][i])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = []
            for k in range(3):
                for p in range(3):
                    if check:
                        if arr[i + k][j + p] in check:
                            return 0
                    check.append(arr[i + k][j + p])
    return 1


for t in range(1, T + 1):
    arr = [list(map(int, input().split(" "))) for _ in range(9)]
    print(f"#{t}", end=" ")
    print(check(arr))

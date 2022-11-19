import sys

sys.stdin = open("10912.txt")

T = int(input())

for tc in range(1, T + 1):
    words = input()

    list_ = []
    for word in words:
        if word not in list_:
            list_.append(word)
        else:
            list_.remove(word)

    if len(list_) != 0:
        print(f"#{tc} ", *(sorted(list_)), sep="")
    else:
        print(f"#{tc} Good")

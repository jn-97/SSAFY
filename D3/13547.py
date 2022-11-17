T = int(input())

for tc in range(1, T + 1):
    fights = input()

    cnt = 0
    for fight in fights:
        if fight == "x":
            cnt += 1
            if cnt > 7:
                print(f"#{tc} NO")
                break
    if cnt <= 7:
        print(f"#{tc} YES")

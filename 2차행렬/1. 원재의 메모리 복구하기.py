T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    n = len(lst)

    while True:
        cnt2 = 0
        for i in lst:
            if i == "0":
                cnt2 += 1
        if cnt2 == 5:
            break
        cnt = 0
        for i in range(n):
            if lst[i] == "1":
                lst[i] = "0"
                cnt += 1
                for j in lst[i+1:]:
                    if j == "0":
                        j = "1"
                    elif j == "1":
                        j = "0"
                    break
                break

    print(f"#{tc} {cnt}")
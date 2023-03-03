"""
2
0011
100
"""


T = int(input())

for tc in range(1, T+1):
    lst = list(input())
    n = len(lst)
    cnt = 0
    flag = False
    while True:

        for i in range(n):
            if lst[i] == "1":
                cnt += 1
                lst[i] = "0"
                for x in range(i+1, n):
                    if lst[x] == "0":
                        lst[x] = "1"
                    else:
                        lst[x] = "0"
                break   # for i


        check = 0
        for j in lst:
            if j == "0":
                check += 1
                if check == n:
                    flag = True
                    break   # for j
        if flag:
            break
    print(f"#{tc} {cnt}")



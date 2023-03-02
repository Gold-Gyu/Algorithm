"""
5
1
2
11
1295
1692
"""
T = int(input())

for tc in range(1, T+1):
    N = input()
    count = [0] * 10
    k = 1
    flag = 0
    while True:
        num = int(N) * k
        strnum = str(num)

        for i in strnum:
            count[int(i)] += 1

        cnt = 0
        for j in range(10):
            if count[j] > 0:
                cnt += 1
                if cnt == 10:
                    break
            else:
                k += 1
                break   # for j
        if cnt == 10:
            break   # while


    print(f"#{tc} {k*int(N)}")



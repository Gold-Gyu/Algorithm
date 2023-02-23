T= int(input())

for tc in range(1, T + 1):
    N = list(input())
    aa = N[:]

    n = len(N)

    for i in range(n // 2):
        N[i], N[n - i - 1] = N[n - i - 1], N[i]

    sr_N = "".join(N)
    sr_aa = "".join(aa)

    cnt = 0
    if sr_N == sr_aa:
        cnt = 1
    else:
        cnt = 0

    print(f"#{tc} {cnt}")
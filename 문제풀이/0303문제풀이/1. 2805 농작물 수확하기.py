import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    ans = 0
    m = n // 2

    # [2] 범위
    s = e = m
    for i in range(n):
        for j in range(s, e+1):
            ans += farm[i][j]

        if i<m:
            s-=1
            e+=1
        else:
            s+=1
            e-=1

    print(f"#{tc} {ans}")



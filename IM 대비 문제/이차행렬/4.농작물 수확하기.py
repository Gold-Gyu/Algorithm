import sys
sys.stdin = open("input.txt" ,"r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(abs(n//2-i), n-abs(n//2-i)):
            cnt += farm[i][j]

    print(f"#{tc} {cnt}")

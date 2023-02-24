T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            ans = 0
            for k in range(i, i+M):
                for h in range(j, j+M):
                    ans += arr[k][h]
            if maxV < ans:
                maxV = ans

    print(f"#{tc} {maxV}")


T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):
            standard = arr[i][j]
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    standard += arr[nr][nc]

            if maxV < standard:
                maxV = standard
    print(f"#{tc} {maxV}")


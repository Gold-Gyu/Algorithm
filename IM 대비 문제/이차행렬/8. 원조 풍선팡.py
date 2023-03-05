T = int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for k in range(4):
                for d in range(1, arr[i][j]+1):
                    nr = i + dr[k] * d
                    nc = j + dc[k] * d
                    if 0 <= nr < N and 0 <= nc < M:
                        s += arr[nr][nc]
            if maxV < s:
                maxV = s

    print(f"#{tc} {maxV}")

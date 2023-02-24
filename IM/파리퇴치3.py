T = int(input())

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 대각선
dr2 = [-1, -1, 1, 1]
dc2 = [-1, 1, -1, 1]


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):

            standard = arr[i][j]
            for k in range(4):
                for h in range(1, M):
                    nr = i + dr[k] * h
                    nc = j + dc[k] * h
                    if 0 <= nr < N and 0 <= nc < N:
                        standard += arr[nr][nc]
            if maxV < standard:
                maxV = standard

            standard2 = arr[i][j]
            for k2 in range(4):
                for h2 in range(1, M):
                    nr = i + dr2[k2] * h2
                    nc = j + dc2[k2] * h2
                    if 0 <= nr < N and 0 <= nc < N:
                        standard2 += arr[nr][nc]
            if maxV < standard2:
                maxV = standard2
    print(f"#{tc} {maxV}")




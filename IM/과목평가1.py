# 가장 높은 봉우리 - 가장 낮은 봉우리

T = int(input())

# 8방향
dr = [0, 1, 0, -1, -1, -1, 1, 1]
dc = [1, 0, -1, 0, -1, 1, -1, 1]


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    minV = 1000
    bong = 0
    for i in range(1, N - 1):
        for j in range(1, N - 1):

            standard = arr[i][j]
            cnt = 0
            for k in range(8):
                nr = i + dr[k]
                nc = j + dc[k]
                if standard > arr[nr][nc]:
                    cnt += 1
                    # cnt = 8이되면

            else:
                if cnt == 8:
                    bong += 1
                    if maxV < standard:
                        maxV = standard
                    if minV > standard:
                        minV = standard

    if bong > 1:
        print(f"#{tc} {maxV - minV}")
    else:
        print(f"#{tc} -1")

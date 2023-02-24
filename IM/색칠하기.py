T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for tc2 in range(N):
        startx, starty, endx, endy, color = map(int, input().split())

        cnt = 0
        for i in range(startx, endx + 1):
            for j in range(starty, endy + 1):
                if arr[i][j] == 0:
                    arr[i][j] = color
                else:   # 곂치면
                    cnt += 1

    print(f"#{tc} {cnt}")


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 도화지의 크기 M 도장

    arr = [[0] * N for _ in range(N)]   # 전체 도화지 생성


    for tc2 in range(M):
        x, y, height, p = map(int, input().split()) # x : 행, y : 열, height : 높이, p : 넓이


        for i in range(x, x + p): # 기준점 x에서 너비 p까지
            for j in range(y, y + height): # 기준점 y에서 높이 height까지
                if arr[i][j] == 0: # 만약 그 좌표 값이 0이면
                    arr[i][j] = 1   # 1씩 색칠해라

        cnt = 0
        for k in range(N):
            for h in range(N):  # 전체 N * N에서
                if arr[k][h] == 1:  # 1로 칠해진 곳이 있으면
                    cnt += 1    # 1씩 카운트


    print(f"#{tc} {cnt}")



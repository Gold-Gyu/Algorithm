from pprint import pprint
T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 초기값 설정
    r, c = 0, 0

    # 우하좌상
    d = 0

    # 숫자 남기기
    for i in range(1, N*N + 1):
        arr[r][c] = i
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r = nr
            c = nc
        else:
            d += 1
            if d == 4:
                d = 0
            r = r + dr[d]
            c = c + dc[d]

    print(f"#{tc}")
    for i in range(N):
        print(*arr[i])


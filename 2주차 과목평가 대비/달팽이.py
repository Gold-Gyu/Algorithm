import sys
sys.stdin = open('input (16).txt', 'r')
from pprint import pprint

T = int(input())

# 우 하 좌
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    # 현재 위치
    r, c = 0, 0

    # 우 하 좌 상의 인덱스 = dx, dy의 인덱스
    d = 0
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

            # 다시 계산해준다.
            nr = r + dr[d]
            nc = c + dc[d]
            r = nr
            c = nc

    pprint(f'#{tc}')
    pprint(arr)
    for i in range(len(arr)):
        print(" ".join(map(str, arr[i])))





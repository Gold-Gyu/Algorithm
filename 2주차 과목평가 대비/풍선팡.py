import sys
sys.stdin = open('input1 (1).txt', 'r')
from pprint import pprint


T = int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N, M = map(int, input().split())


    arr = [list(map(int, input().split())) for _ in range(N)]
    # N * M 크기 만들기
    # 기준점
    maxV = 0
    for i in range(N):
        for j in range(M):
            # cnt = arr[i][j] # cnt = 2
            cnt = 0
            # 우 하 좌 상
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < M:
                    cnt += arr[nx][ny]


            if maxV < cnt:
                maxV = cnt

    print(f"#{tc} {maxV}")

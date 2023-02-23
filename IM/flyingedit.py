import sys
sys.stdin = open('in1.txt', 'r')
from pprint import pprint

T = int(input())

# 우 하 좌 상

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dx2 = [-1, 1, 1, -1]
dy2 = [-1, -1, 1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N):
        for j in range(N):

            cnt = field[i][j]
            for k in range(4):
                for h in range(1, M):
                    nx = i + dx[k] * h
                    ny = j + dy[k] * h
                    nx2 = i + dx2[k] * h
                    ny2 = j + dy2[k] * h
                    if 0 <= nx < N and 0 <= ny < N and 0 <= nx2 < N and 0 <= ny2 < N:
                        cnt += field[nx][ny]


                    if 0 <= nx < N and 0 <= ny < N:
                        cnt += field[nx][ny]

            if maxV < cnt:
                maxV = cnt

    print(f"#{tc} {maxV}")
import sys
sys.stdin = open('input (5).txt', 'r')
from pprint import pprint

T = int(input())

dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]

for tc in range(1, T+1):
    N, M, K, H = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):  # continue를 만나서 돌아오는 곳
            rocket = field[i][j]
            maxV = 0
            minV = 10000
            can_find = True
            for x in range(8):      # 8방향 탐색
                nx = i + dx[x]
                ny = j + dy[x]
                if 0 <= nx < N and 0 <= ny < M:
                    if maxV < field[nx][ny]:
                        maxV = field[nx][ny]
                    if minV > field[nx][ny]:
                        minV = field[nx][ny]
                else:
                    can_find = False
                    break
            if not can_find:
                continue

            if maxV - minV <= K and minV <= rocket and (rocket - minV) <= H:
                cnt += 1
                print(i, j, K, H, rocket-minV)

    print(f"#{tc} {cnt}")
    """
    
    """

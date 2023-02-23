import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

# 우 하 좌 상
nx = [0, 1, 0, -1]
ny = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0

    for i in range(N):
        for j in range(M):

            cnt = arr[i][j]
            for k in range(4):
                ni = i + nx[k]
                nj = j + ny[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            if maxV < cnt:
                maxV = cnt

    print(f"#{tc} {maxV}")

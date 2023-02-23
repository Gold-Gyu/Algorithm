import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())

dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 예비 후보지는 8개의 방향 중 사진을 찍을 수 있는 방향이 4방향 이상인 지점으로 정함
    ans = 0
    for x in range(N):
        for y in range(M):
            cnt = arr[x][y]

            cnt2 = 0
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < M:
                    if cnt > arr[nx][ny]:
                        cnt2 += 1

            if cnt2 >= 4:
                ans += 1
    print(f"#{tc} {ans}")
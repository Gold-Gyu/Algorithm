T = int(input())

# 8방향
# 우 하 좌 상 대각선 위 좌 우, 대각선 아래 좌 우
dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    maxV = 0                    # 최대값
    minV = 11                   # 최솟값
    count = 0                   # 봉우리 갯수
    for i in range(1, N-1):     # 가장자리 구역은 판단할 수 없기 떄문에 범위는 1, N-1
        for j in range(1, N-1): # 가장자리 구역은 판단할 수 없기 떄문에 범위는 1, N-1 # 따라서 범위 설정 따로 필요 없음!
            standard = arr[i][j]    # 비교 기준
            cnt = 0                 # 기준이 각 주변보다 크면 +1 해줄 cnt
            for k in range(8):      # 8 방향 탐색
                nx = i + dx[k]      # 8 방향의 x 좌표
                ny = j + dy[k]      # 8 방향의 y 좌표
                if standard > arr[nx][ny]:  # 기준 보다 작은 갯수
                    cnt += 1        # 8방향마다 기준보다 작은 곳 발견 시 1씩 계산해서 8개가 된다면 봉우리로 인정
                    if cnt == 8:    # 주변이 다 기준보다 작다면
                        count += 1  # 봉우리로 인정

                        if maxV < standard:
                            maxV = standard
                        if minV > standard:
                            minV = standard


    if count <= 1:          # 봉우리가 1개거나 그 미만이면 -1
        print(f"#{tc} -1")
    else:                   # 봉우리가 2개 이상이면
        print(f"#{tc} {maxV- minV}")    # 최대값과 최솟값의 차이
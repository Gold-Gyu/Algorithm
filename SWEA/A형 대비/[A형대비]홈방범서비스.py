T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 # 집의 개수를 센다
    maxV = 0
    K = 0

    # 일단 모든지점에서 완전탐색
    # 이후 한번 1이 있는 곳 시도해보기(집이 있는 곳을 찾는다.)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1

            while M * cnt >= K:  # 수익에서 벗어나기 전까지 마름모 모양으로 탐색하며 집의 개수 찾기
                # 비용을 계산
                K += 1
                n = K
                K = K * K + (K - 1) * 2

                # 마름모 탐색
                # 시작점(i - (n-1), j)
                for x in range(n):  # n == 3, 0 1 2


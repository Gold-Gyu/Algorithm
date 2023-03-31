T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 3개 영역으로 나누기
    minV = 2500
    for a in range(N - 2):  # w 영역 맨아래 0 ~ N-3까지
        for b in range(a + 1, N - 1):  # b 영역 a+1 ~ N-2까지
            cnt = 0  # 각 영역에서 새로 칠하는 횟수
            for i in range(a + 1):  # W영역에서
                for j in range(M):
                    if arr[i][j] != "W":
                        cnt += 1
            for i in range(a + 1, b + 1):  # b영역에서
                for j in range(M):
                    if arr[i][j] != "B":
                        cnt += 1
            for i in range(b + 1, N):  # R영역에서
                for j in range(M):
                    if arr[i][j] != "R":
                        cnt += 1

            if minV > cnt:  # 현재의 영역에서 새로 칠할 칸
                minV = cnt

    print(f"#{tc} {minV}")
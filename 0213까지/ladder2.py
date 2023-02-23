import sys
sys.stdin = open('input (14).txt', 'r')

from pprint import  pprint


# 1순위 고려사항 : 좌 or 우가 나오면 이동
# 방향 설정?

T = 10
for tc in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    minV = 100 * 100
    for sj in range(1, 101):
        si = 0
        # [1] 시작지점 찾기
        if arr[si][sj] != 1:
            continue
        cnt, dj = 0, 0
        ci, cj = si, sj

        while ci < 99:
            cnt += 1
            if dj == 0:
                if arr[ci][cj-1] == 1:  #좌측
                    dj = -1 # 방향 좌측
                    cj -= 1
                elif arr[ci][cj+1] == 1:    # 우측
                    dj = 1  # 방향 우측
                    cj += 1
                else:
                    ci += 1

            else:
                if arr[ci][cj+dj] == 1:
                    cj += dj
                else:   #진행방향이 막힌 경우 아래로
                    dj = 0
                    ci += 1
        if minV >= cnt:
            minV, ans = cnt, sj -1

    print(f"#{tc} {ans}")
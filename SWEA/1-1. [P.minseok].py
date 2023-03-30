dr = [0, 1]
dc = [1, 0]

# 유효성 판단
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

def solve(r, c, now_sum):   # r, c 시작점, now_sum: 지금까지의 합
    global min_sum

    if (r, c) == (n - 1, n - 1):    # 맨 오른쪽 끝에 도착하면
        # 최소값 구하기
        min_sum = min(min_sum, now_sum)
        return

    # 다음 위치로 이동(오른쪽 or 아래)
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc):
            solve(nr, nc, now_sum + arr[nr][nc])


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    min_sum = 10000
    solve(0, 0, arr[0][0])

    print(f"#{tc} {min_sum}")
T = int(input())



def is_valid(r,c):
    return 0 <= r < n and 0 <= c < m


arr = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0

# 모든 ㅟ치에서 풍선 다 터트려 보고 그 중에서 최대값 구하기

for r in range(n): # 행
    for c in range(n) # 열
        # 현재 꽃가루 수 + 상하좌우 꽃가루 수
        cnt = arr[r][c]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 위치가 배열의 범위를 벗어나지 않는지 꼭 검사해야함
            if is_valid(nr, nc):
                cnt += arr[nr][nc]

        if max_cnt < cnt:
            max_cnt = cnt

    print(f"#{tc} {max_cnt}")
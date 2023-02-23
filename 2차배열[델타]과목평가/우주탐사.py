
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    visited = [[0]]

    r, c = 0, 0

    d = area[0][0]

    energy = [d]

    # 더 이상 움직일 수 없을 때까지 반복
    while True:
    # 현재 에너지를 기록
    # 이전 방향과 다를 경우에만 기록한다.
        if energy[-1] != d:
            energy.append(d)

        # 다음 위치 계산
            nr = r + dr[d]
            nc = c + dc[d]

        # 다음 위치 검사해서 유효하면 위치 이동
        if is_valid(nr, nc):
            # 방문체크
            visited[nr][nc] = 1
            # 현재 위치를 다음 위치로 바꾸기
            r, c = nr, nc
            # 방향도 다음 방향으로 바꿔준다.
            d = area[nr][nc]
        # 유효한 위치가 아니면 탐색중단
        else:
            break
    print(f"#{tc} ", end ="")
    print(*energy, sep = " ")

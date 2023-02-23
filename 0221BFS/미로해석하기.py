


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    maze = [list(map(int, input())) for _ in range(n)]

    # 시작위치 (2인 위치)찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                r, c = i, j

    # 함수 안쓰고 bfs
    # 큐 초기화
    # 시작위치 큐에 넣고 방문체크
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((r, c))
    visited[r][c] = 1
    # 거리 계산
    distance = -1

    # 중간에 답을 찾았는지
    find = False

    # 큐가 빌때까지 반복
    while q:
        # 현재 단계에서 큐의 길이(원소의개수)를 통해 해당 단계에서 반복횟수를 제한
        size = len(q)
        distance += 1
        # 해당 단계에서만 반복하도록 반복문 하나 추가
        for _ in range(size):
            # 위치 하나 꺼내기
            r, c = q.pop(0)

            # 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 다음 위치가 유효한지 벽이 아닌지, 방문한적 없는지
                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    # 만약 다음 위치가 목표 위치
                    if maze[nr][nc] == 3:
                        q = []
                        find = True
                        break
            if find:
                break

    # 만약 중간에 도착지점을 만나지 못한경우는 답이 0
    if not find:
        distance = 0

    print(f"#{tc} {distance}")
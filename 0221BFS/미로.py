T = int(input())

for tc in range(1, T+1):
    n = int(input())

    maze = [list(map(int, input())) for _ in range(n)]

    r, c = 0, 0

    # 시작위치(2인 위치) 찾기

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

    # 거리 계싼싼

    distance = -1

    # 큐가 빌떄까지 반복
    while q:
        # 현재 단계에서 큐의 길이(원소의 개수)를 통해 해당 단계에서 반복횟수를 제한
        size = len(q)

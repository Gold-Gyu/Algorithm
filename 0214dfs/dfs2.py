dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, n):
    # 방문 체크 배열 또한 2차원
    visited = [[0] * n for i in range(n)]
    # stack 초기화
    stack = []
    visited[r][c] = 1

    while True:

        for i in range(n):
            for j in range(n):
                if (i, j) == (r, c):
                    print("★", end = " ")
                else:
                    print(visited[i][j], end = " ")
            print()

        if arr =






        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음 위치 계산후, 갈 수 있는 곳인지 그리고 이전에 방문하지 않았던 곳인지 확인
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and not visited[nr[nc]]:
                # 돌아올 위치를 스택에 저장(현재 위치)
                stack.append((r,c))
                # 방문체크
                visited[nr][nc] = 1
                # 다음 위치로 이동
                r, c = nr, nc
            # 다른 방향 탐색 X, 갈 수 있는 방향으로 계속 간다.
            break

        # 4 방향을 살펴봤는데 갈 수 있는 곳이 없다?
        else:

            # 내가 전에 돌아올 위치를 저장했었는데 그것을 스택에서 꺼낸다.
            if stack:
                r, c = stack.pop()

            # 스택에 남아있는 위치가 없다면 탐색 종료
            else:
                break
# 0은 길, 1은 벽, 3은 도착지점
arr = [[0, 0, 0, 0, 1, 3],
       [1, 1, 1, 0, 1, 1],
       [0, 0, 1, 0, 1, 0],
       [0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 0]]

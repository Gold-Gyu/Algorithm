def bfs(i, j):
    visited[i][j] = 1
    q = []
    q.append((i, j))

    while q:
        size = len(q)

        for i in range(size):
            r, c = q.pop(0)
            for k in range(4):
                nr = r + di[k]
                nc = c + dj[k]
                if 0 <= nr < M and 0 <= nc < N and farm[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    for tc2 in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1

    cnt = 0
    flag = False
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)

    print(cnt)

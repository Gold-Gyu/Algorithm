from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        size = len(q)
        for i in range(size):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and field[nr][nc] > num:
                    q.append((nr, nc))
                    visited[nr][nc] = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
for x in range(N):
    if maxV < max(field[x]):
        maxV = max(field[x])

maxV2 = 0
for num in range(maxV):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if field[i][j] > num and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)
    if maxV2 < cnt:
        maxV2 = cnt

print(maxV2)

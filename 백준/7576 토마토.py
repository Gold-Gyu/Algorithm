from collections import deque
from pprint import pprint

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

q = deque()
for i in range(M):
    for j in range(N):
        if field[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1
        elif field[i][j] == -1:
            visited[i][j] = 1

while q:
    size = len(q)
    for x in range(size):
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N and field[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

answer = 0
cnt = 0
flag = False
for i in range(M):
    for j in range(N):
        if answer < visited[i][j]:
            answer = visited[i][j]-1
        elif visited[i][j]:
            cnt += 1
            if cnt == (N*M):
                answer = 0
        elif visited[i][j] == 0:
            answer = -1
            flag = True
            break   # for j
    if flag:
        break


print(answer)



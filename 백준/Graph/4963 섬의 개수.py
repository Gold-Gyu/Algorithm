from pprint import pprint
from collections import deque
# 8방향

def bfs(i, j):
    visited[i][j] = 1
    q = deque()
    q.append((i, j))

    while q:
        size = len(q)
        for i in range(size):
            r, c = q.popleft()
            for k in range(8):
                nr = r + di[k]
                nc = c + dj[k]
                if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == 0 and land[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = 1

di = [0, 1, 0, -1, -1, -1, 1, 1]
dj = [1, 0, -1, 0, -1, 1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0 # 8방향에 1이없는 섬들의 갯수
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)
    print(cnt)

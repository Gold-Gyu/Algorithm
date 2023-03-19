from pprint import pprint
from collections import deque

def bfs(i, j):
    q = deque()
    visited[i][j] = default
    q.append((i, j))

    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and field[nr][nc] == 1:
                    visited[nr][nc] = default
                    q.append((nr, nc))



dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())

field = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt = 0 # 단지 갯수
default = 0 # 각 단지내 집의 수 세기 위
for i in range(N):
    for j in range(N):
        if field[i][j] == 1 and visited[i][j] == 0:
            default += 1
            cnt += 1
            bfs(i, j)
print(cnt)

answer = []
for num in range(1, default+1):
    cnt2 = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y] == num:
                cnt2 += 1
    answer.append(cnt2)
ans = sorted(answer)

for a in ans:
    print(a)
from pprint import pprint
from collections import deque
dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]

def is_valid(nr, nc):
    return 0 <= nr < n and 0 <= nc < m

def bfs(i, j):

    q = deque()
    q.append((i, j))
    flag = 0

    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid(nr, nc) and arr[r][c] >= arr[nr][nc] and not v[nr][nc]:
                    if flag == 0:
                        q.append((nr, nc))
                        v[nr][nc] = 1
                elif is_valid(nr, nc) and arr[r][c] > arr[nr][nc] and not v[nr][nc]:
                    flag = 1



n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
ans = 0


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and v[i][j] == 0:
            bfs(i, j)

print(ans)
# 산봉우리가 몇개인지 세야한다.
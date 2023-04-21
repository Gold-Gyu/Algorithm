from pprint import pprint
from collections import deque
def bfs(i, j):
    global maxV
    ans = 0
    flag = 0
    v = [[0] * m for _ in range(n)]
    q = deque()
    q.append((i, j))
    v[i][j] = 1

    while q:
        ans += 1
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0 and v[nr][nc] == 0:
                    q.append((nr, nc))
                    v[nr][nc] = 1
                elif 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and v[nr][nc] == 0:
                    flag = 1
        if maxV < ans:
            maxV = ans
        if flag:
            return


dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

maxV = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            bfs(i, j)
print(maxV)
import sys
from sys import stdin
from collections import deque


def is_valid(nr, nc):
    return 0 <= nr < n and 0 <= nc < m

def bfs(r, c):
    global maxV

    ans = 0
    v = [[0] * m for _ in range(n)]
    q = deque()
    q.append((r, c))
    v[r][c] = 1

    while q:

        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            # if v[r][c] < maxV:
            #     return
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid(nr, nc) and arr[nr][nc] == "L" and v[nr][nc] == 0:
                    v[nr][nc] = v[r][c] + 1

                    q.append((nr, nc))

        ans += 1
    if maxV < ans:
        maxV = ans


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

maxV = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            bfs(i, j)

print(maxV-1)


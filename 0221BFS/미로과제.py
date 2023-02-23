import sys
sys.stdin = open('input (7).txt', 'r')
from pprint import pprint

T = 10

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_valid(r, c):
    return 0 <= r < 16 and 0 <= c < 16

for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    r, c = 0, 0

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                r, c = i, j

    visited = [[0] * 16 for _ in range(16)]
    q = []
    q.append((r, c))
    visited[r][c] = 1

    path = 1

    find = False
    while q:
        n = len(q)

        for _ in range(n):
            r, c = q.pop(0)

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if is_valid(nr, nc) and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    if arr[nr][nc] == 3:
                        q = []
                        find = True
                        break
            if find:
                break
    if not find:
        path = 0

    print(f"#{tc} {path}")


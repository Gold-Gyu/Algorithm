import sys
sys.stdin = open("보급로.txt", "r")

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

def bfs(start, end):

    global minV
    q = deque()
    v = [[10000] * n for _ in range(n)]
    q.append((start, end))
    v[start][end] = arr[start][end]

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if v[nr][nc] > v[r][c] + arr[nr][nc]:
                    q.append((nr, nc))
                    v[nr][nc] = v[r][c] + arr[nr][nc]
    return v[n-1][n-1]

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    # arr을 하나씩 원소로 만들기
    ans = bfs(0, 0)
    print(f"#{tc} {ans}")
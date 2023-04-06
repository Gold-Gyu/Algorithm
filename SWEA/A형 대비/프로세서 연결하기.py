import sys
sys.stdin = open("프로세서 연결하기.txt", "r")

from collections import deque


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


def bfs(r, c):
    global line_cnt, line
    cnt = 0
    q = deque()

    q.append((r, c))
    v[r][c] = 1

    while q:
        size = len(q)
        for i in range(size):
            r, c = q.popleft()

            for k in range(4):
                for h in range(1, n):
                    nr = r + dr[k] * h
                    nc = c + dc[k] * h
                    if is_valid(nr, nc) and arr[nr][nc] == 0:
                        line_cnt += 1   # 전설의 길이
                        cnt += 1
                        q.append((nr, nc))
                        # 방문함수 필요없나?
                    else:
                        line_cnt -= cnt

                if line_cnt == abs(r-n-1) + abs(c-n-1):
                    line += 1
                    return



T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for tc in range(1, T+1):
    n = int(input()) # 프로세서 개수
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0] * n for _ in range(n)]

    minV = 9999999  # 최소값
    line_cnt = 0
    line = 0    # 전선이 못나오는 행
    col = []    # 전선이 못나오는 열

    for r in range(1, n-1):
        for c in range(1, n-1):
            if arr[r][c] == 1 and v[r][c] == 0:
                bfs(r, c)
                # 여기서 4방향 탐색?
                line += line_cnt
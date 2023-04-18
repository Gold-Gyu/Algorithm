from pprint import pprint
from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < h and 0 <= nc < w

def bfs(fire, o, p):
    global cnt
    global flag

    q = deque(fire)
    # q.append(fire)
    q2 = deque()
    q2.append((o, p))

    while True:
        size = len(q)
        for i in range(size):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid(nr, nc) and (field[nr][nc] == "@" or field[nr][nc] == "."):
                    v[nr][nc] = 1
                    field[nr][nc] = "*"
                    q.append((nr, nc))

        size = len(q2)  # 상근
        for i in range(size):
            r, c = q2.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 > nr or nr >= h or 0 > nc or nc >= w:
                    flag = 1
                    return
                elif is_valid(nr, nc) and v[nr][nc] == 0 and field[nr][nc] == ".":
                    field[nr][nc] = "@"
                    q2.append((nr, nc))

        cnt += 1
        if len(q2) == 0:    # 더 이상 움직일 곳이 없다
            flag = 2
            return

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    w, h = map(int, input().split())
    field = [list(input()) for _ in range(h)]
    v = [[0] * w for _ in range(h)]
    fire = []
    cnt = 1
    flag = 1
    ans = "IMPOSSIBLE"
    for i in range(h):
        for j in range(w):
            if field[i][j] == "@":
                o = i
                p = j
            elif field[i][j] == "*":
                v[i][j] = 1
                fire.append((i, j))

    bfs(fire, o, p)
    if flag == 1:
        print(cnt)
    elif flag == 2:
        print(ans)

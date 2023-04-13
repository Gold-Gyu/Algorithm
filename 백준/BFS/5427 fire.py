from pprint import pprint
from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < h and 0 <= nc < w

def fire_bfs(fire):
    q = deque(fire)

    while q:
        size = len(q)
        for i in range(size):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid(nr, nc) and v[nr][nc] == 0 and (field[nr][nc] == "." or field[nr][nc] == "@"):
                    v[nr][nc] = 1
                    field[nr][nc] = "*"
                    q.append((nr, nc))
        return

def person_bfs(i, j):
    global cnt
    global flag
    global ans
    q = deque()
    q.append((i, j))

    while q:
        size = len(q)
        for i in range(size):
            x, y = q.popleft()
            for k in range(4):
                nx = x + dr[k]
                ny = y + dc[k]
                if v[nx][ny] == 0 and field[nx][ny] == ".":
                    q.append((nx, ny))
                    field[nx][ny] = "@"
                elif not is_valid(nx, ny):
                    flag = 1
                    return
                else:
                    ans = "IMPOSSIBLE"

            cnt += 1
            return


T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for tc in range(1, T+1):
    w, h = map(int, input().split())
    field = [list(input()) for _ in range(h)]
    v = [[0] * w for _ in range(h)]
    pprint(field)
    fire = []
    flag = 0
    cnt = 0
    ans = ""
    for i in range(h):
        for j in range(w):
            if field[i][j] == "@":
                o = i
                p = j
            elif field[i][j] == "*":
                v[i][j] = 1
                fire.append((i, j))
    # r, c 시작점을 구했음
    while True:
        fire_bfs(fire)
        person_bfs(o, p)
        if flag == 1:
            print(cnt)
            break
        elif flag == 2:
            print(ans)


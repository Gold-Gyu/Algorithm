from collections import deque
from pprint import pprint
def find_knight(x, y):
    global cnt
    v = [[0] * l for _ in range(l)]
    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            if r == movex and c == movey:
                return
            for nr, nc in [(r-2, c+1), (r-1, c+2), (r+1, c+2), (r+2, c+1), (r-2, c-1), (r-1, c-2), (r+1, c-2), (r+2, c-1)]:
                if 0 <= nr < l and 0 <= nc < l and v[nr][nc] == 0:
                    q.append((nr, nc))
                    v[nr][nc] = 1
        cnt += 1

T = int(input())



for tc in range(1, T+1):
    cnt = 0
    l = int(input())
    nowx, nowy = map(int, input().split())
    movex, movey = map(int, input().split())
    if nowx == movex and nowy == movey:
        print(0)
    else:
        find_knight(nowx, nowy)
        print(cnt)
from pprint import pprint
from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != -1

def wind1(x, y):
    v = [[0] * m for _ in range(n)]
    d = 0

    while True:
        nx = x + dr[d]
        ny = y + dc[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == -1:
            return
        elif 0 <= nx < n and 0 <= ny < m:
            v[nx][ny] = arr[nx][ny]
            if arr[x][y] == -1:
                arr[nx][ny] = 0
            else:
                arr[nx][ny] = v[x][y]
            x = nx
            y = ny
        else:
            d -= 1
            if d == -1:
                d = 3

def wind2(x, y):
    v = [[0] * m for _ in range(n)]
    d = 0

    while True:
        nx = x + dr[d]
        ny = y + dc[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == -1:
            return
        elif 0 <= nx < n and 0 <= ny < m:
            v[nx][ny] = arr[nx][ny]
            if arr[x][y] == -1:
                arr[nx][ny] = 0
            else:
                arr[nx][ny] = v[x][y]
            x = nx
            y = ny
        else:
            d += 1
            if d == 4:
                d = 0

def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                tmp = 0 #
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if is_valid(nx, ny):
                        v[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp

    for i in range(n):
        for j in range(m):
            arr[i][j] += v[i][j]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

up = -1
down = -1
# 공기 청정기 위치 찾기
for i in range(n):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

dust = []
cleaning = []
for T in range(t):

    spread() # 확산
    pprint(arr)
    wind1(up, 0)
    wind2(down, 0)
    # 바람 부는 것
    # 위에 것
    pprint(arr)
    print("=============================")
    v = [[0] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            cnt += arr[i][j]

print(cnt)
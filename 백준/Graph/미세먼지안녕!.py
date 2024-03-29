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


    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                tmp = 0 # 4방향으로 퍼질 수 있을 때 퍼지는 양
                for k in range(4):
                    nx = dr[k] + i
                    ny = dc[k] + j
                    if is_valid(nx, ny):    # 범위 안에 있고 공기청정기 위치가 아니라면
                        v[nx][ny] += arr[i][j] // 5 # 방문함수에 퍼지는 값들을 다 더해서 나타내고
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp    # 퍼졌을 때 자기 위치에서 줄어든 먼지의 양, tmp는 4방향중 퍼진 횟수만큼 합이 더해져있음

    # 다 퍼트렸으면
    # v함수 : 주변으로 퍼트렸던 먼지들의 합
    # arr함수 : 처음 먼지가 퍼지면서 줄어든 양
    # 두 개를 더해서 1초에 먼지가 퍼졌을 때 먼지들의 양을 구한다.
    for i in range(n):
        for j in range(m):
            arr[i][j] += v[i][j]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


# 공기 청정기 위치 찾기
for i in range(n):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

for T in range(t):

    spread() # 확산
    wind1(up, 0)
    wind2(down, 0)

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            cnt += arr[i][j]

print(cnt)
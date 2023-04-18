from pprint import pprint
from collections import deque
"""

7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0

"""
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

def bfs():

    q = deque(dust)
    while q:

        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            cnt = 0
            # 먼지 있는 곳에서
            # 4방향 탐색
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid(nr, nc):
                    v[nr][nc] += (arr[r][c] // 5)
                    cnt += 1
            # 4방향 탐색했으면 자기 자신은 조건대로 깍기
            # 방문함수에 퍼진 먼지를
            # 본체 함수에는 부모먼지의 줄어든 양을 나타내서
            # 더한다.
            arr[r][c] = arr[r][c] - ((arr[r][c] // 5) * cnt)


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
dust = []
cleaning = []
for T in range(t):
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                dust.append((i, j)) # 먼지가 있는 곳들 전부다 집어넣기
            elif arr[i][j] == -1:
                cleaning.append((i, j))
    bfs() # 확산

    for i in range(n):
        for j in range(m):
            arr[i][j] += v[i][j]
    pprint(arr)

    x, y = cleaning[0]
    wind1(x, y)
    x, y = cleaning[1]
    wind2(x, y)
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





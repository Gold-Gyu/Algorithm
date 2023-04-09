from collections import deque
import copy

def is_valid(nr, nc):
    return 0 <= nr < n and 0 <= nc < n

def bfs(i, j, s):
    global checkpoint
    global cnt
    city = copy.deepcopy(arr)
    v2 = copy.deepcopy(v)

    q = deque()
    q.append((i, j))
    v2[i][j] = 1
    s += city[i][j]

    while q:
        size = len(q)
        for x in range(size):
            o, p = q.popleft()
            for k in range(4):
                nr = o + dr[k]
                nc = p + dc[k]
                if is_valid(nr, nc) and v2[nr][nc] == 0 and l <= abs(city[o][p] - city[nr][nc]) <= r:
                    q.append((nr, nc))
                    v2[nr][nc] = 1
                    s += city[nr][nc]
                    cnt += 1
                    checkpoint += 1
    change(s, v2)

def change(s, v2):

    ans = s // cnt
    for i in range(n):
        for j in range(n):
            if v2[i][j] == 1:
                arr[i][j] = ans


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
count = 0
cp = 0
checkpoint = 0
cnt = 1
while cp < n*n:

    for i in range(n):
        for j in range(n):
            bfs(i, j, 0)
            if checkpoint == 0:
                cp += 1
    if cnt >= 2:
        count += 1
    cnt = 1
    checkpoint = 0
print(count)
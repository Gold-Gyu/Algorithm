from collections import deque
from pprint import pprint

def spread(num):
    q = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                q.append((i, j))
                v[i][j] = 1

    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < n and 0 <= nc < n and v[nr][nc] == 0 and arr[nr][nc] == 0:
                    arr[nr][nc] = num



dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
s, x, y = map(int, input().split())
flag = 0

if arr[x-1][y-1]:
    print(arr[x-1][y-1])
else:
    for second in range(s):
        for num in range(1, k+1):
            spread(num)
            if arr[x - 1][y - 1]:
                flag = 1
                break
        if flag:
            break
    print(arr[x - 1][y - 1])

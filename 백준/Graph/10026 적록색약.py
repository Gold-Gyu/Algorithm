from pprint import pprint
from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < n and 0 <= nc < n

def normal():
    global ans1
    v = [[0] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0 and arr[i][j] == "R":
                q.append((i, j))
                v[i][j] = 1
                ans1 += 1

                while q:
                    size = len(q)
                    for _ in range(size):
                        r, c = q.popleft()
                        for k in range(4):
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if is_valid(nr, nc) and arr[nr][nc] == "R" and v[nr][nc] == 0:
                                v[nr][nc] = 1
                                q.append((nr, nc))

            elif v[i][j] == 0 and arr[i][j] == "B":
                q.append((i, j))
                v[i][j] = 1
                ans1 += 1

                while q:
                    size = len(q)
                    for _ in range(size):
                        r, c = q.popleft()
                        for k in range(4):
                            nx = r + dr[k]
                            ny = c + dc[k]
                            if is_valid(nx, ny) and arr[nx][ny] == "B" and v[nx][ny] == 0:
                                v[nx][ny] = 1
                                q.append((nx, ny))

            elif v[i][j] == 0 and arr[i][j] == "G":
                q.append((i, j))
                v[i][j] = 1
                ans1 += 1
                while q:
                    size = len(q)
                    for _ in range(size):
                        r, c = q.popleft()
                        for k in range(4):
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if is_valid(nr, nc) and arr[nr][nc] == "G" and v[nr][nc] == 0:
                                v[nr][nc] = 1
                                q.append((nr, nc))

def RG():
    global ans2
    v = [[0] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0 and arr[i][j] == "R":
                q.append((i, j))
                v[i][j] = 1
                ans2 += 1

                while q:
                    size = len(q)
                    for _ in range(size):
                        r, c = q.popleft()
                        for k in range(4):
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if is_valid(nr, nc) and (arr[nr][nc] == "R" or arr[nr][nc] == "G") and v[nr][nc] == 0:
                                v[nr][nc] = 1
                                q.append((nr, nc))

            elif v[i][j] == 0 and arr[i][j] == "B":
                q.append((i, j))
                v[i][j] = 1
                ans2 += 1

                while q:
                    size = len(q)
                    for _ in range(size):
                        r, c = q.popleft()
                        for k in range(4):
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if is_valid(nr, nc) and arr[nr][nc] == "B" and v[nr][nc] == 0:
                                v[nr][nc] = 1
                                q.append((nr, nc))

            if v[i][j] == 0 and arr[i][j] == "G":
                q.append((i, j))
                v[i][j] = 1
                ans2 += 1

                while q:
                    size = len(q)
                    for _ in range(size):
                        r, c = q.popleft()
                        for k in range(4):
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if is_valid(nr, nc) and (arr[nr][nc] == "G" or arr[nr][nc] == "R") and v[nr][nc] == 0:
                                v[nr][nc] = 1
                                q.append((nr, nc))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n = int(input())
arr = [list(input()) for _ in range(n)]

ans1 = 0
ans2 = 0

normal()
RG()
print(ans1, ans2)
from pprint import pprint
from collections import deque

def escape():
    global ans
    v = [[0] * c for _ in range(r)]
    q = deque()
    q2 = deque()
    # 물의 위치를 다 담아준다
    for i in range(r):
        for j in range(c):
            if arr[i][j] == "*":
                q.append((i, j))
                v[i][j] = 1
            elif arr[i][j] == "S":
                q2.append((i, j))
    # 물이 퍼지는 과정 +
    while q2:

        # 물이 퍼지는 과정
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and (arr[nx][ny] == "." or arr[nx][ny] == "S") and v[nx][ny] == 0:
                    v[nx][ny] = 2
                    arr[nx][ny] = "*"
                    q.append((nx, ny))

        ans += 1
        size0 = len(q2)
        for _ in range(size0):
            x1, y1 = q2.popleft()

            for k in range(4):
                nx = x1 + dx[k]
                ny = y1 + dy[k]
                if 0 <= nx < r and 0 <= ny < c and (arr[nx][ny] == "." or arr[nx][ny] == "D") and v[nx][ny] == 0:
                    if arr[nx][ny] == "D":
                        return print(ans)
                    arr[x1][y1] = "."
                    arr[nx][ny] = "S"
                    q2.append((nx, ny))
        if len(q2) == 0:
            return print("KAKTUS")



dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
ans = 0
escape()


"""
3 3
D.*
...
.S.

"""
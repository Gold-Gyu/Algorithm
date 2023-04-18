from collections import deque
from pprint import pprint
def is_valid(nr, nc):
    return 0 <= nr < n and 0 <= nc < n

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n = int(input())
board = [[0] * n for _ in range(n)]
v = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = -1

l = int(input())

time_direction = []
for _ in range(l):
    x, c = input().split()
    time_direction.append((x, c))
# 시작점
start = end = 0
v[start][end] = 1
time = 0
d = 0   # 처음에 우를 바라본다
direction_index = 0
q = deque() # 꼬리 맨 끝
q.append((start, end))

while True:

    x = time_direction[direction_index][0]
    c = time_direction[direction_index][1]
    if int(x) == time:
        direction_index += 1
        if len(time_direction) == direction_index:
            direction_index = 0
        if c == "L":
            d -= 1
            if d == -1:
                d = 3
        elif c == "D":
            d += 1
            if d == 4:
                d = 0

    time += 1
    nr = start + dr[d]
    nc = end + dc[d]
    if is_valid(nr, nc):
        if v[nr][nc] == 1:
            break
        elif board[nr][nc] == 0:
            tail_x, tail_y = q.popleft()
            v[tail_x][tail_y] = 0
            v[nr][nc] = 1
            q.append((nr, nc))
            start = nr
            end = nc
        elif board[nr][nc] == -1:
            board[nr][nc] = 0
            v[nr][nc] = 1
            q.append((nr, nc))
            start = nr
            end = nc


    elif not is_valid(nr, nc) or v[nr][nc] == 1:
        break



print(time)

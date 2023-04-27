from collections import deque
from pprint import pprint
import copy

# 바깥 공기에서 4방향 탐색해서 치즈가 있는 곳들은 체크한다.
#


def cheezeremove(x, y): # 바깥 공기에서부터 치즈가 있는 곳들을 체크해서 바꿔주는 함수
    v2 = copy.deepcopy(v)
    q = deque()
    q.append((x, y))
    v2[x][y] = 1

    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < n and 0 <= nc < m: # 범위 안이고
                    if v2[nr][nc] == 0 and arr[nr][nc] == 0: # 공기이면
                        q.append((nr, nc))  # 넣어서 다시 4방탐색
                        v2[nr][nc] = 1
                    elif v[nr][nc] == 0 and arr[nr][nc] == 1:
                        v2[nr][nc] = -1

    for i in range(n-1):
        for j in range(m-1):
            if v2[i][j] == -1:
                arr[i][j] = 0


def check():
    global nums
    global arrborn_cnt
    num = 0

    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i, j))
    size = len(q)
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                num += 1
                break # for k

        if num == size and count == 1:
            nums = arrborn_cnt

        elif num == size:
            nums = size


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
arrborn = copy.deepcopy(arr)
arrborn_cnt = 0
for x in range(n):
    for y in range(m):
        if arrborn[x][y] == 1:
            arrborn_cnt += 1

v = [[0] * m for _ in range(n)]
count = 0
nums = 0
flag = 0
for o in range(n):
    for p in range(m):
        if arr[o][p] == 1:
            flag = 1
            break
    if flag:
        break

if flag:
    while True:
        count += 1
        cnt = 0
        flag = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    cnt += 1
                    flag = 1    # 치즈가 1개 이상 있다면
                    break   # for j

            if flag:    # for i
                break

        if cnt == 0:
            break
        else:   # 치즈가 1개 이상있다면
            cheezeremove(0, 0)
            check()
    if count == 2:
        nums = arrborn_cnt
    print(count-1)
    print(nums)
else:
    print(0)
    print(0)

"""
5 5 
0 0 0 0 0 
0 1 1 0 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0


"""


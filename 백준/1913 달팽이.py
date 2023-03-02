from pprint import pprint
# 하 우 상
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
T = int(input())
N = int(input())

# 전체판
arr = [[0] * T for _ in range(T)]

# 시작점
r, c = 0, 0
d = 0
for i in range(T*T, 0, -1):
    arr[r][c] = i
    if arr[r][c] == N:  # 35
        x, y = r, c
    nr = r + dr[d]
    nc = c + dc[d]
    if 0 <= nr < T and 0 <= nc < T and arr[nr][nc] == 0:
        r = nr
        c = nc
    else:
        d += 1
        if d == 4:
            d = 0
        r = r + dr[d]
        c = c + dc[d]

for ans in arr:
    print(*ans)
print(x+1, y+1)

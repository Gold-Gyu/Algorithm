from collections import deque

def is_valid(nr, nc):
    return 0 <= nr < R and 0 <= nc < C

def bfs(stair, r, c):
    global ans
    global flag2

    q = deque()
    q.append((stair, r, c))
    v[stair*R+r][c] = 1

    while q:
        ans += 1
        size = len(q)

        for i in range(size):
            stair, x, y = q.popleft()

            # 4방향 갈 수 있는 곳
            for k in range(4):
                nr = x + dr[k]
                nc = y + dc[k]

                if is_valid(nr, nc) and (floor[stair][nr][nc] == "." or floor[stair][nr][nc] == "E") and v[stair*R + nr][nc] == 0:
                    q.append((stair, nr, nc))
                    v[stair*R + nr][nc] = 1
                    if floor[stair][nr][nc] == "E":
                        return
            # 상하층
            if floor_cnt > 1:
                if stair == 0:
                    stair = stair + height
                    if floor_cnt > stair:
                        if is_valid(x, y) and floor[stair][x][y] == "." and v[stair*R + x][y] == 0:
                            q.append((stair, x, y))
                            v[stair*R + x][y] = 1

                elif stair > 0:
                    stairup = stair + height
                    if floor_cnt > stairup:
                        if is_valid(x, y) and floor[stairup][x][y] == "." and v[stairup * R + x][y] == 0:
                            q.append((stairup, x, y))
                            v[stairup * R + x][y] = 1
                        elif floor[stairup][x][y] == "E":
                            return
                    stairdown = stair - height
                    if stairdown >= 0:
                        if is_valid(x, y) and floor[stairdown][x][y] == "." and v[stairdown * R + x][y] == 0:
                            q.append((stairdown, x, y))
                            v[stairdown * R + x][y] = 1

                        elif floor[stairdown][x][y] == "E":
                            return
        if len(q) == 0:
            flag2 = 1
            return


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
height = 1

while True:
    ans = 0
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break
    floor = []
    for _ in range(L):
        floor.append([list(input()) for _ in range(R)])
        blank = input()
    floor_cnt = len(floor)  # 층의 개수
    v = [[0] * C for _ in range(R * C)]
    here = 0    #층 인덱스
    flag = 0
    flag2 = 0

    for stair in range(floor_cnt):
        for r in range(R):
            for c in range(C):
                if floor[stair][r][c] == "S":

                    bfs(stair, r, c)
                    flag = 1
                    break
            if flag:
                break
        if flag:
            break
    if flag == 1 and flag2 == 0:
        print(f"Escaped in {ans} minute(s).")
    elif flag2 and flag:
        print("Trapped!")
"""
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

0 0 0

"""
import copy
from pprint import pprint
from collections import deque
def is_valid(nr, nc):
    return 0 <= nr < R and 0 <= nc < C

def bfs(stair, r, c):
    global ans
    global flag2

    q = deque()
    q.append((stair, r, c))
    v[stair*R+r][stair*C+c] = 1

    while q:
        ans += 1
        size = len(q)

        for i in range(size):
            stair, r, c = q.popleft()

            # 4방향 갈 수 있는 곳
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if is_valid(nr, nc) and floor[stair][nr][nc] != "#" and v[stair*R + nr][nc] == 0:
                    q.append((stair, nr, nc))
                    v[stair*R + nr][nc] = 1
            # 상하층
            if floor_cnt > 1:
                if stair == 0:
                    stair = stair + height
                    if floor_cnt > stair:
                        if floor[stair][r][c] == "." and v[stair*R + r][c] == 0:
                            q.append((stair, r, c))
                            v[stair*R + r][c] = 1
                            stair = stair - height
                elif stair > 0:
                    stair = stair + height
                    if floor_cnt > stair:
                        if is_valid(r, c) and floor[stair][r][c] == "." and v[stair * R + r][c] == 0:
                            q.append((stair, r, c))
                            v[stair * R + r][c] = 1
                        elif floor[stair][r][c] == "E":
                            return
                        stair = stair - height*2
                        if is_valid(r, c) and floor[stair][r][c] == "." and v[stair * R + r][c] == 0:
                            q.append((stair, r, c))
                            v[stair * R + r][c] = 1
                            stair = stair - height * 2
                        elif floor[stair][r][c] == "E":
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

    if L == R == C == 0:
        break
    floor = []
    for _ in range(L):
        floor.append([list(input()) for _ in range(R)])
        blank = input()
    floor_cnt = len(floor)  # 층의 개수
    v = [[0] * C for _ in range(R * C + floor_cnt)]
    here = 0    #층 인덱스
    flag = 0
    flag2 = 0

    for stair in range(floor_cnt):
        for r in range(R):
            for c in range(C):
                if floor[stair][r][c] == "S":
                    v[stair*R + r][c] = 1
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



import sys
sys.stdin = open("탈주범검거.txt", "r")
from pprint import pprint
from collections import deque

def is_valid(r, c):
    return 0 <= r < m and 0 <= c < n


def bfs(r, c):

    q = deque()
    q.append((r, c))
    v[r][c] = 1

    while q:
        if l in v:
            break
        size = len(q)
        for i in range(size):
            r, c = q.popleft()
            if arr[r][c] == 1:
                for k in range(4):
                    nr = r + dr1[k]
                    nc = c + dc1[k]
                    if is_valid(nr, nc) and v[nr][nc] == 0 and arr[nr][nc]:
                        if nr == r + dr1[0] and nc == r + dc1[0]:#우
                            if arr[nr][nc] in (1, 3, 6, 7):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        elif nr == r + dr1[1] and nc == r + dc1[1]:#하
                            if arr[nr][nc] in (1, 2, 4, 7):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        elif nr == r + dr1[2] and nc == r + dc1[2]:#좌
                            if arr[nr][nc] in (1, 3, 4, 5):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        elif nr == r + dr1[3] and nc == r + dc1[3]:#상
                            if arr[nr][nc] in (1, 2, 5, 6):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1
            if arr[r][c] == 2:
                for k in range(2):
                    nr = r + dr2[k]
                    nc = c + dc2[k]
                    if is_valid(nr, nc) and v[nr][nc] == 0 and arr[nr][nc]:
                        if nr == r + dr2[0] and nc == r + dc2[0]:  # 우
                            if arr[nr][nc] in (1, 2, 5, 6):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        if nr == r + dr1[1] and nc == r + dc1[1]:  # 하
                            if arr[nr][nc] in (1, 2, 4, 7):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1
            if arr[r][c] == 3:
                for k in range(2):
                    nr = r + dr3[k]
                    nc = c + dc3[k]
                    if is_valid(nr, nc) and v[nr][nc] == 0 and arr[nr][nc]:
                        if nr == r + dr3[0] and nc == r + dc3[0]:  # 우
                            if arr[nr][nc] in (1, 4, 5, 3):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        if nr == r + dr3[1] and nc == r + dc3[1]:  # 하
                            if arr[nr][nc] in (1, 3, 6, 7):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

            if arr[r][c] == 4:
                for k in range(2):
                    nr = r + dr4[k]
                    nc = c + dc4[k]
                    if is_valid(nr, nc) and v[nr][nc] == 0 and arr[nr][nc]:
                        if nr == r + dr4[0] and nc == r + dc4[0]:  # 우
                            if arr[nr][nc] in (1, 2, 5, 6):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        if nr == r + dr4[1] and nc == r + dc4[1]:  # 하
                            if arr[nr][nc] in (1, 3, 6, 7):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

            if arr[r][c] == 5:
                for k in range(2):
                    nr = r + dr5[k]
                    nc = c + dc5[k]
                    if is_valid(nr, nc) and v[nr][nc] == 0 and arr[nr][nc]:
                        if nr == r + dr5[0] and nc == r + dc5[0]:  # 우
                            if arr[nr][nc] in (1, 2, 4, 7):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        if nr == r + dr5[1] and nc == r + dc5[1]:  # 하
                            if arr[nr][nc] in (1, 3, 6, 7):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

            if arr[r][c] == 6:
                for k in range(2):
                    nr = r + dr6[k]
                    nc = c + dc6[k]
                    if is_valid(nr, nc) and v[nr][nc] == 0 and arr[nr][nc]:
                        if nr == r + dr6[0] and nc == r + dc6[0]:  # 우
                            if arr[nr][nc] in (1, 2, 4, 7):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        if nr == r + dr6[1] and nc == r + dc6[1]:  # 하
                            if arr[nr][nc] in (1, 3, 4, 5):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1
            if arr[r][c] == 7:
                for k in range(2):
                    nr = r + dr7[k]
                    nc = c + dc7[k]
                    if is_valid(nr, nc) and v[nr][nc] == 0 and arr[nr][nc]:
                        if nr == r + dr7[0] and nc == r + dc7[0]:  # 우
                            if arr[nr][nc] in (1, 2, 5, 6):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1

                        if nr == r + dr7[1] and nc == r + dc7[1]:  # 하
                            if arr[nr][nc] in (1, 3, 4, 5):
                                q.append((nr, nc))
                                v[nr][nc] = v[r][c] + 1
T = int(input())

dr1 = [0, 1, 0, -1]
dc1 = [1, 0, -1, 0]

dr2 = [-1, 1]
dc2 = [0, 0]

dr3 = [0, 0]
dc3 = [-1, 1]

dr4 = [-1, 0]
dc4 = [0, 1]

dr5 = [-1, 0]
dc5 = [0, 1]

dr6 = [-1, 0]
dc6 = [0, -1]

dr7 = [1, 0]
dc7 = [0, -1]

for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0] * m for _ in range(n)]
    cnt = 0
    bfs(r, c)
    print(v)
    for i in range(n):
        for j in range(m):
            if v[i][j]:
                cnt += 1

    print(f"#{tc} {cnt}")
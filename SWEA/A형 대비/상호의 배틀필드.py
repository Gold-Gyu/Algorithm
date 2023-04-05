import sys
sys.stdin = open("상호의 배틀필드.txt", "r")


def is_valid(r, c):
    return 0 <= r < h and 0 <= c < w

def bfs(r, c):


    for i in lstn:
        cnt = 0
        if i == "S":    # S가 나오면

            if field[r][c] == "^":
                while True:
                    r -= 1  # 그 자리에서
                    cnt += 1
                    if not is_valid(r, c):
                        break
                    if field[r][c] == "*":
                        field[r][c] = "."
                        break
                    elif field[r][c] == "#":
                        break # while

                r += cnt
                cnt = 0

            elif field[r][c] == "v":
                while True:
                    r += 1
                    cnt -= 1
                    if not is_valid(r, c):
                        break

                    if field[r][c] == "*":
                        field[r][c] = "."
                        break
                    elif field[r][c] == "#":
                        break  # while

                r += cnt
                cnt = 0

            elif field[r][c] == "<":
                while True:
                    c -= 1
                    cnt += 1
                    if not is_valid(r, c):
                        break
                    if field[r][c] == "*":
                        field[r][c] = "."
                        break
                    elif field[r][c] == "#":
                        break  # while

                c += cnt
                cnt = 0

            elif field[r][c] == ">":

                while True:
                    c += 1
                    cnt -= 1
                    if not is_valid(r, c):
                        break
                    if field[r][c] == "*":
                        field[r][c] = "."
                        break
                    elif field[r][c] == "#":
                        break # while

                c += cnt
                cnt = 0
        elif i == "U":  # U가 나오면    1. 방향을 위로 바꾸고 2. 그 위가 .이면 이동한다.
            nr = r + dr[3]
            nc = c + dc[3]
            if not is_valid(nr, nc):
                nr = nc = 0
            elif is_valid(nr, nc) and field[nr][nc] != ".":
                field[r][c] = "^"
                nr = nc = 0
            elif is_valid(nr, nc) and field[nr][nc] == ".":
                field[r][c] = "."
                field[nr][nc] = "^"
                r, c = nr, nc
                nr = nc = 0


        elif i == "D":
            nr = r + dr[1]
            nc = c + dc[1]
            if not is_valid(nr, nc):
                nr = nc = 0
            elif is_valid(nr, nc) and field[nr][nc] != ".":
                field[r][c] = "v"
                nr = nc = 0
            elif is_valid(nr, nc) and field[nr][nc] == ".":
                field[r][c] = "."
                field[nr][nc] = "v"
                r, c = nr, nc
                nr = nc = 0


        elif i == "L":
            nr = r + dr[2]
            nc = c + dc[2]
            if not is_valid(nr, nc):
                nr = nc = 0
            elif is_valid(nr, nc) and field[nr][nc] != ".":
                field[r][c] = "<"
                nr = nc = 0
            elif is_valid(nr, nc) and field[nr][nc] == ".":
                field[r][c] = "."
                field[nr][nc] = "<"
                r, c = nr, nc
                nr = nc = 0



        elif i == "R":
            nr = r + dr[0]
            nc = c + dc[0]
            if not is_valid(nr, nc):
                nr = nc = 0
            elif is_valid(nr, nc) and field[nr][nc] != ".":
                field[r][c] = ">"
                nr = nc = 0
            elif is_valid(nr, nc) and field[nr][nc] == ".":
                field[r][c] = "."
                field[nr][nc] = ">"
                r, c = nr, nc
                nr = nc = 0

    return


T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for tc in range(1, T+1):
    h, w = map(int, input().split())
    field = [list(input()) for _ in range(h)]
    n = int(input())
    lstn = list(input())
    flag = 0
    for r in range(h):
        for c in range(w):
            if field[r][c] in ("^", "v", "<", ">"):
                bfs(r, c)
                flag = 1
                break
        if flag:
            break
    print(f"#{tc}", end=" ")
    for i in range(h):
        print(*field[i], sep="")

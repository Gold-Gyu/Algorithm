# import sys
# sys.stdin = open("상호의 배틀필드.txt", "r")


def is_valid(r, c):
    return 0 <= r < h and 0 <= c < w

def bfs(r, c):

    for command in lstn:
        cnt = 0
        if command == "S":    # S가 나오면

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

        elif command == "U":  # U가 나오면    1. 방향을 위로 바꾸고 2. 그 위가 .이면 이동한다.
            nr = r + dr[3]
            nc = c + dc[3]

            if is_valid(nr, nc):
                if field[nr][nc] != ".":
                    field[r][c] = "^"

                elif field[nr][nc] == ".":
                    field[r][c] = "."
                    field[nr][nc] = "^"
                    r, c = nr, nc
            else:
                field[r][c] = "^"

        elif command == "D":
            nr = r + dr[1]
            nc = c + dc[1]
            if is_valid(nr, nc):
                if field[nr][nc] != ".":
                    field[r][c] = "v"

                elif field[nr][nc] == ".":
                    field[r][c] = "."
                    field[nr][nc] = "v"
                    r, c = nr, nc
            else:
                field[r][c] = "v"

        elif command == "L":
            nr = r + dr[2]
            nc = c + dc[2]
            if is_valid(nr, nc):
                if field[nr][nc] != ".":
                    field[r][c] = "<"

                elif field[nr][nc] == ".":
                    field[r][c] = "."
                    field[nr][nc] = "<"
                    r, c = nr, nc
            else:
                field[r][c] = "<"

        elif command == "R":
            nr = r + dr[0]
            nc = c + dc[0]

            if is_valid(nr, nc):
                if field[nr][nc] != ".":
                    field[r][c] = ">"

                elif field[nr][nc] == ".":
                    field[r][c] = "."
                    field[nr][nc] = ">"
                    r, c = nr, nc
            else:
                field[r][c] = ">"
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

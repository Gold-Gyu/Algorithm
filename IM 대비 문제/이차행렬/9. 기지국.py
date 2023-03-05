T = int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for tc in range(1, T+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if field[r][c] == "A":
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if field[nr][nc] == "H":
                            field[nr][nc] = "X"

            elif field[r][c] == "B":
                for k in range(4):
                    for d in range(1, 3):
                        nr = r + dr[k] * d
                        nc = c + dc[k] * d
                        if 0 <= nr < N and 0 <= nc < N:
                            if field[nr][nc] == "H":
                                field[nr][nc] = "X"

            elif field[r][c] == "C":
                for k in range(4):
                    for d in range(1, 4):
                        nr = r + dr[k] * d
                        nc = c + dc[k] * d
                        if 0 <= nr < N and 0 <= nc < N:
                            if field[nr][nc] == "H":
                                field[nr][nc] = "X"
    cnt = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] == "H":
                cnt += 1

    print(f"#{tc} {cnt}")

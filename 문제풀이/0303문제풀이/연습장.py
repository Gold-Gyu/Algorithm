T = int(input())

dr = [0, 1, 0, -1, -1, -1, 1, 1]
dc = [1, 0, -1, 0, -1, 1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = "NO"
    cnt = 0
    flag = False
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "o":
                for k in range(8):
                    cnt = 1
                    for h in range(1, 5):
                        nr = r + dr[k] * h
                        nc = c + dc[k] * h
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == "o":
                            cnt += 1
                            if cnt == 5:
                                flag = True
                                break   # for h
                    if flag:
                        break # for k
                if flag:
                    break   # for c
        if flag:
            break # for r
    if cnt == 5:
        ans = "YES"

    print(f"#{tc} {ans}")
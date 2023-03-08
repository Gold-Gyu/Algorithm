T = int(input())

di = [0, 1, 1, -1]
dj = [1, 1, 0, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = "NO"

    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                for k in range(4):
                    cnt = 1
                    for h in range(1, 5):
                        ni = i + di[k] * h
                        nj = j + dj[k] * h
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == "o":
                            cnt += 1

                    if cnt == 5:
                        ans = "YES"
    print(f"#{tc} {ans}")
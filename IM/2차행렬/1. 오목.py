# 특정 조건을 가지는 최대, 최소
# 카운트배열에 넣고
# 다시 영역에

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr =[input() for _ in range(N)]

    # 시작돌 찾기
    ans = "NO"
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":    # 돌을 만나면
                for di, dj in[[0, 1], [1, 1], [1, 0], [1, -1]]:
                    cnt = 1
                    ni, nj = i + di, j + dj
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == "o":
                        cnt += 1
                        ni, nj = ni + di, nj + dj
                        if cnt == 5:
                            ans = "YES"
                            break       # while을 빠져나가는 break
                    if ans == "YES":
                        break   # for di, dj
            if ans == "YES":
                break  # for j
        if ans == "YES":
            break  # for i

    print(f"#{tc} {ans}")


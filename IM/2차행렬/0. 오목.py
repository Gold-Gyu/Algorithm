import sys
sys.stdin = open("sample_input (17).txt", "r")

def gogo(N):

    for i in range(N):
        for j in range(N):
            if field[i][j] == "o":
                for k in range(4):  # 4방향 탐
                    cnt = 1
                    for h in range(1, 5):
                        ni = i + dr[k] * h
                        nj = j + dc[k] * h
                        if 0 <= ni < N and 0 <= nj < N and field[ni][nj] == "o":
                            cnt += 1
                    if cnt == 5:
                        return "YES"
    return "NO"


T = int(input())

dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

for tc in range(1, T+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    ans = gogo(N)
    # 일단 기본적으로 다 돈다
    print(f"#{tc} {ans}")




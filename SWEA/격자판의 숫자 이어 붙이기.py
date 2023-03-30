import sys
sys.stdin = open("격자판의 숫자 이어 붙이기.txt", "r")

def f(idx, idy, cnt, result):
    global count
    if cnt == 6:
        count += 1
        return

    for k in range(4):
        nr = idx + dr[k]
        nc = idy + dc[k]
        if 0 <= idx < 4 and 0 <= idy < 4:
            result.append(field[nr][nc])
            f(nr, nc, cnt+1, result)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    field = [list(map(int, input().split())) for _ in range(4)]
    result = []
    cnt = 0
    count = 0
    for i in range(4):
        for j in range(4):
            result.append(field[i][j])
            f(i, j, cnt, result)

    print(count)
from pprint import pprint


T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
arr = [[0] * 102 for _ in range(102)]
for tc in range(1, T+1):
    x, y = map(int, input().split())

    for i in range(x+1, x+11):
        for j in range(y+1, y+11):
            if arr[i][j] == 0:
                arr[i][j] = 1

cnt = 0
for i in range(102):
    for j in range(102):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 102 and 0 <= nj < 102 and arr[ni][nj] == 1 and arr[i][j] == 0:
                cnt += 1

print(cnt)





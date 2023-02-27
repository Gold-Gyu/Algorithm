import sys
sys.stdin = open('sample_input (8).txt', 'r')
from pprint import pprint

T = int(input())

dr = [0, 1, 0, -1, -1, -1, 1, 1]
dc = [1, 0, -1, 0, -1, 1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    pprint(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] != ".":
                visited[i][j] = 1

    # 행
    ans = "NO"
    for k in range(N):
        cnt = 0
        for h in range(N):
            if visited[k][h] == 1:
                cnt += 1
                if cnt == 5:
                    ans = "YES"

    # 열
    for o in range(N):
        cnt2 = 0
        for p in range(N):
            if visited[p][o] == 1:
                cnt2 += 1
                if cnt2 == 5:
                    ans = "YES"

    # 좌 대
    cnt3 = 0
    for i in range(N):
        if visited[i][i] == 1:
            cnt3 += 1
            if cnt3 == 5:
                ans = "YES"

    # 우 대
    cnt4 = 0
    for j in range(N-1, -1, -1):
        if visited[j][j] == 1:
            cnt4 += 1
            if cnt4 == 5:
                ans = "YES"
    pprint(visited)
    print(ans)


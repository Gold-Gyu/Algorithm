import sys
sys.stdin = open('sample_input (8).txt', 'r')
from pprint import pprint

# 둘러쌓기 (패딩할 때) 주의할점
# 1. 범위 잘 적어놓을 것
# 2.



T = int(input())

dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = "NO"
    flag = False
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "o":
                for k in range(4):
                    cnt = 1
                    for h in range(1, 5):
                        nr = r + dr[k] * h
                        nc = c + dc[k] * h
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == "o":
                            cnt += 1

                    if cnt == 5:
                        ans = "YES"
                        flag = True
                        break # for k
            if flag:
                break   # for c
        if flag:
            break # for r


    print(f"#{tc} {ans}")
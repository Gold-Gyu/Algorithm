import sys
sys.stdin = open("sample_input (3).txt", "r")
from pprint import pprint


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N :세로, M : 가로
    flag = [list(input()) for _ in range(N)]
    ans = 0
    wans = 0    # 첫 열 바꿀 개수
    bcnt = 0
    wcnt = 0
    # 국기의 첫번째 줄 white
    # 국기의 두번째 줄 ~ 마지막 - 1 줄까지 확인
    # 국기의 마지막 줄 red
    for i in range(1):
        for j in range(M):
            if flag[i][j] != "W":
                wans += 1
    ans += wans         # 첫 행 끝

    for v in range(N-1, N): # 마지막 행 끝
        wcnt = 0
        for o in range(M):
            if flag[v][o] == "W":
                wcnt += 1
        ans += M - wcnt

    # 2 ~ N -1  행
    for i in range(1, N-1):
        bcnt = 0    # blue 개수
        wcnt = 0    # white 개수
        rcnt = 0    # red 개수
        for j in range(M):
            if flag[i][j] == "W":   # 흰색이 있으면
                wcnt += 1           # 1식 증가
            elif flag[i][j] == "B": # 블루가 있으면
                bcnt += 1           # 1씩 증가

        # 행을 다 돌았을 때
        if bcnt > wcnt:     # 이 행 파란색으로 칠하기. 이 아래로는 Red와 Blue 갯수 비교하기
            # 그 행에서의 전체 블록 갯수에서 블루 갯수 빼기
            ans += M - bcnt # blue로 칠해야하는 블록의 개수

            # 여기서부터 파랑과 빨강 갯수 비교해서 파랑 칠할 지 빨강 칠할 지 확인
            for q in range(i+1, N-1):         # 파랑 줄 아래로 검사
                redcount = 0                  # 빨강 갯수
                bcnt = 0                      # 파랑 갯수
                for w in range(M):
                    if flag[q][w] == "R":
                        redcount += 1
                    elif flag[q][w] == "B":
                        bcnt += 1
                if bcnt > redcount:           # 파랑색 칠하기
                    ans += M - bcnt
                elif redcount > bcnt:
                    ans += M - redcount
                    for y in range(q+1, N-1):
                        redcount = 0
                        bcnt = 0
                        wcnt = 0
                        for u in range(M):
                            if flag[y][u] == "R":
                                redcount += 1
                            elif flag[y][u] == "B":
                                bcnt += 1
                        if redcount > bcnt:
                            ans += M - redcount
        elif bcnt == wcnt and i != N-1:
            for b in range(i+1, i+2):
                wcnt = 0
                bcnt = 0
                for s in range(M):
                    if flag[b][s] == "W":
                        wcnt += 1
                    elif flag[b][s] == "B":
                        bcnt += 1
                if wcnt > bcnt:
                    ans += wcnt







    print(ans)
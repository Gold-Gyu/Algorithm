import sys
sys.stdin = open("격자판의 숫자 이어 붙이기.txt", "r")



# 문자열보다 정수로하는 것이 더 빠르다

def dfs(idx, startpoint_value, i, j):

    if idx == 7:
        sset.add(startpoint_value) # 중복제거
        return

    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(idx + 1, startpoint_value * 10 + field[nr][nc], nr, nc)
            # 10을 곱하는 이유?
# 델타 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    field = [list(map(int, input().split())) for _ in range(4)]
    sset = set()    # 중복제거를 위해 만듬, 정답을 위한

    # 임의 위치에서 == 모든 위치에서
    for i in range(4):
        for j in range(4):
            dfs(1, field[i][j], i, j)
    ans = len(sset)
    print(f"#{tc} {ans}")
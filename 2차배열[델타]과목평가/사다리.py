import sys
sys.stdin = open('input (18).txt', 'r')
from pprint import pprint

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    # 시작점 구하기
    x, y = 0, 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                x, y = i, j
    visited[x][y] = 1
    # 시작점에서부터 좌우 살피면서
    # 올라가기 + 방문 기록하기 (방문한곳 방문 x)
    while x > 0:
        if 0 <= y-1 and arr[x][y-1] == 1 and visited[x][y-1] == 0:
            y -= 1
            visited[x][y] = 1
        # 만약 오른쪽을 갈 수 있으면
        elif y+1 < 100 and arr[x][y + 1] == 1 and visited[x][y+1] == 0:
            y += 1
            visited[x][y] = 1
        elif 0 <= x < 100:
            x -= 1
            visited[x][y] = 1

    print(f"#{tc} {y}")
"""
1
0 1 0 0 0
0 1 0 0 0
0 1 1 1 0
0 0 0 1 0
0 0 0 1 2
"""
from pprint import pprint

N, M = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(N)]

pprint(ice)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 탐색을 다 한다.
for i in range(N):
    for j in range(M):
        if ice[i][j]:
            bfs()
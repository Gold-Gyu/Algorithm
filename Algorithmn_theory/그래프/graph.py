from pprint import pprint

"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

"""


def dfs1(v, k):  # 중복없이 빠짐없이
    visited[v] = 1  # 중복방지용
    print(v)
    for w in adjL[v]:  # v와 인접한 점들 꺼내서
        if visited[w] == 0:  # 방문한적이 없는 w면
            dfs1(w, k)
    """        
    인접 행렬일 때

    for w in range(1, k+1): # 전체 정점을 다 돌면서
        if adjM[v][w] == 1 and visited[w] == 0: # 인접한 정점이 있고, 방문한적이없으면
            dfs1(w, k)
    """


def dfs2(s, k):  # s :시작점, V번까지 있는
    stack = []
    visited = [0] * (k + 1)
    v = s

    while True:
        if visited[v] == 0:
            print(v)
            visited[v] = 1
        # 현재 정점에서 갈 수 있는 곳을 탐색한다.
        for w in range(1, k + 1):
            # 갈 수 있는 w정점이 있으면
            if adjM[v][w] and visited[w] == 0:
                stack.append(v)
                v = w
                break

        else:  # 더 이상 인접의 정점이 없으면
            if stack:  # 스택이 비어있찌 않으면
                v = stack.pop()
            else:  # 스택이 비어있으면
                break
    return


def dfs3(v, k, g):
    global cnt
    print(v, k, g)
    if v == g:
        print("1")
        cnt += 1  # 목적지에 도착횟수
    else:
        visited[v] = 1  # 중복방지용
        for w in range(1, k + 1):
            if adjM[v][w] == 1 and visited[w] == 0:
                dfs3(w, k, g)
        visited[v] = 0


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1
    adjL[n1].append(n2)
    adjL[n2].append(n1)
visited = [0] * (V + 1)
cnt = 0
# pprint(adjM)
# print(adjL)


dfs1(1, V)
print("============")
dfs2(1, V)
print("============")
dfs3(1, V, 7)
print(cnt)
from collections import deque
import copy

def bfs(i, j):
    q = deque() # 큐를 생성하고
    union = []  # 연합나라의 위치를 다 넣어준다.
    q.append((i, j))
    union.append((i, j))

    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()  # q에서 하나 꺼내서
            for k in range(4): # 4 방향 탐색하고
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:  # 범위를 벗어나지 않고 방문한적이없고
                    if l <= abs(arr[nx][ny] - arr[x][y]) <= r:  # 인구차이가 범위 안에 있다면
                        v[nx][ny] = 1 # 방문처리 해주고
                        q.append((nx, ny))  # 큐에 넣어준다 == 연합국이다. == 인구이동한다.
                        union.append((nx, ny))  # 연합국에 가입.
    return union    # 연합국(즉, 인구이동해야하는 좌표들)




# 4방향 탐색
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


year = 0
while True:
    v = [[0] * n for _ in range(n)] # 방문함수 제작 + 매번 싸이클마다 초기화
    flag = 0    # 체크포인트 생성 + 사이클마다 초기화
    for i in range(n):
        for j in range(n):  # 모든 경우의 수를 돌면서
            if v[i][j] == 0: # 한번도 방문하지 않은 곳에서
                v[i][j] = 1 # 이제 방문했다고 체크
                union_ = bfs(i, j) # bfs를 돌아 인구이동하는 연합 나라의 개수를 구한다.

                if len(union_) > 1:    # 연합국가가 있다면( 즉, 이동해야하는 국가가 있다면)
                    flag = 1 # 인구이동이 있으면 체크!!!
                    sum_ = sum(arr[x][y] for x, y in union_)    # 연합국가들이 가지고 있는 사람들의 수 다 더한다.
                    country = len(union_)   # 연합국가의 수
                    human = sum_ // country

                    for x, y in union_:
                        arr[x][y] = human
    if flag == 0:
        break
    year += 1


print(year)

from collections import deque
# 반복은 더 이상 인구이동이 없을 때까지
# 4방향 탐색
# 인구차이가 L명 이상 R명 이하면
# 하루동안 opengate

# 방문함수 찍으면서 cnt + 1 == 연합을 이루고 있는 타일의 개수
# 타일안에

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(i, j):
    global s
    global cnt
    q = deque()
    q.append((i, j))

    s += people[i][j]

    while q:
        size = len(q)
        for z in range(size):
            i, j = q.popleft()
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if is_valid(nr, nc):
                    if v[nr][nc] == 0:
                        if l <= abs(people[nr][nc] - people[i][j]) <= r:
                            s += people[nr][nc]
                            v[i][j] = 1
                            v[nr][nc] = 1
                            q.append((nr, nc))
                            cnt += 1 # 타일의 개수

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
openday = 0
cnt = 1
s = 0
flag = 0

# 1. 모든 곳을 돌면서 상하좌우를 비교해서 조건에 맞으면 방문함스체크 + 타일개수

while True:
    end = 0
    for i in range(n):
        for j in range(n):
            bfs(i, j)   # 연합의 개수, 연합 확인용 방문함수 체크, 연합 명수 총
            if cnt <= 1:    # 바꿀게없다면
                end += 1
            else:   # 바꿀게 있다
                end = 0
                cnt2 = 0
                for o in range(n):
                    for p in range(n):
                        if v[o][p] == 1:
                            people[o][p] = s // cnt
                            v[o][p] = 0
                s = 0
                cnt = 1
    openday += 1
    if end == n*n:
        break



print(openday)


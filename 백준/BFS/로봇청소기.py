
def is_valid(nr, nc):
    return 0 <= nr < n and 0 <= nc < m

def dfs(r, c, d):

    v[r][c] = 1    # 처음 장소 방문체크 및 청소했음을 커밋

    while True:
        cnt = 0 # 4방향에 0이있고 가본적이 없는 곳이 있는지 확인
        cp = 0  # 4방향 다 돌았는지 체크하는 변수 + while때마다 초기화
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if is_valid(nr, nc) and arr[nr][nc] == 0 and v[nr][nc] == 0:
                cnt += 1    # 4방향 중 청소해야하는 빈 장소가 있다면
                break   # 더 이상 4방향 탐색 정지

        if cnt: # 4방향 중 방문해서 청소해야하는 장소가 있다면
            while True: # 반복한다.
                d -= 1  # 반시계 방향 90도 한 후 전진
                if d == -1:
                    d = 3
                r = r + dr[d]
                c = c + dc[d]
                if is_valid(r, c) and arr[r][c] == 0 and v[r][c] == 0:  # 만약 벽이 아니고 방문한적도 없고 범위 안이면
                    v[r][c] = 1 # 방문하여 청소한다.
                    break   # while : 반시계방향으로 도는 과정을 중지

                # 반시계방향 전환 후 직진했을 때 갈 수 없다면(방문했거나, 벽이거나) 다시 자리 원상복귀
                r = r - dr[d]
                c = c - dc[d]
                cp += 1 # 4방향 중 1번 확인했음
                if cp == 4: # 이 과정 즉, 반시계방향 전환 후 직진했을 때 갈 수 없는 상황이 4번 발생했다는 말은 이제 더 이상 방문할 수 있는 곳이 없음을 의미
                    # 따라서 이제는 자신의 방향에서 뒤로 이동해야함
                    r = r - dr[d]
                    c = c - dc[d]
                    if arr[r][c] == 1:  # 뒤로 이동했는데 벽이라면
                        return  # 전체과정 끝
                    # 벽이 아니라면 뒤로 이동한 좌표를 가지고 while문 탈출
                    break
        else:   # 방문할 곳이 없다면
            # 빼주기
            r = r - dr[d]
            c = c - dc[d]
            if arr[r][c] == 1:
                return

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
ans = 0

dfs(r, c, d)

for i in range(n):
    for j in range(m):
        if v[i][j]:
            ans += 1
print(ans)





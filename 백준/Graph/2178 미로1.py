def bfs(r, c):
    visited = [[0] * M for _ in range(N)]   # 방문함수 생성(갔던곳 재방문 방지)
    q = []  # 큐 생성
    q.append((r, c))  # 큐안 에 넣기
    visited[r][c] = 1 # 시작점 방문 체크

    cnt = 1     # 몇번째에 도착했는 구하기
    while q:
        size = len(q)   # 큐 안에 들어있는 갯수만큼 빼준다

        for i in range(size):
            r, c = q.pop(0)    # 큐에서 좌표 빼주기

            if r == N-1 and c == M-1:
                print(cnt)
                q = []
                break

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == "1":
                    q.append((nr, nc))
                    visited[nr][nc] = 1
        cnt += 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int,input().split())
arr = [input() for _ in range(N)]

bfs(0, 0)





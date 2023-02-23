import sys
sys.stdin = open('sample_input(1) (3).txt', 'r')

def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q = []  # 큐 생성
    q.append((i, j))  # 시작점 인큐  q = [(i,j)]
    visited[i][j] = 1  # 시작점 인큐 표시
    while q:  # 큐가 비어있지 않으면
        i, j = q.pop(0)  # 디큐
        if maze[i][j] == '3':  # 도착하면 1리턴
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 인접하고(벽이아니고) 방문안한 칸이 있으면
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[i][j] != '1' and visited[ni][nj] == 0:
                q.append((ni, nj))  # 현재칸 주변의 이동가능한 통로 좌표를 큐에 넣고 방문예정
                visited[ni][nj] = visited[i][j] + 1
    return 0


for _ in range(10):
    tc = int(input())
    maze = [input() for _ in range(16)]
    si = sj = -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
                break  # for j
        if si != -1:  # 출발점을 찾아서 중단된 경우
            break  # for i

    ans = bfs(si, sj, 16)
    print(f'#{tc} {ans}')
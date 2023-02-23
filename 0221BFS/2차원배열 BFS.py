
dr = [-1, 1, 0, 0]

dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

# sr: 시작행
# sc: 시작열

def bfs(sr, sc):
    visited = [[0] * n for _ in range(n)]

    q = []
    q.append((sr, sc))  # 시작점 sr, sc를 큐에 삽입
    visited[sr][sc] = 1

    day = 0
    while q:
        # 원소를 반환하기 전에 현재 단계에서 큐의 원소를 몇개까지하면되는지
        size = len(q)
        for _ in range(size):

            r, c = q.pop(0) # 큐에서 첫 번째 원소를 반환

            # 현재 위치를 어떻게 가는지 보여주는 코드

            for i in range(n):
                for j in range(n):
                    if (i, j) == (r, c):
                        print("★", end = "")
                    else:
                        print(maze[i][j], end = " ")

                print()

            print("===================")

            if maze[r][c] == 3:
                print(f"탈출 : {day}")
                q = []
                break
            # 현재 위치 r, c에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 유효한 인덱스, 벽이 아니여야아함, 방문한적도 없어야함
                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))  # 큐에넣기
                    visited[nr][nc] = 1 # 방문체크
        day += 1

n = 7

maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 3, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 1],
        ]

"""
dfs일 떄



"""

bfs(0, 0)


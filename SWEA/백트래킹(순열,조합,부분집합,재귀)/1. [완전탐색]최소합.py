
from collections import deque

def bfs(r, c):
    global sum_
    q = deque()
    q.append((r, c))
    sum_ += arr[r][c]

    while q:
        size = len(q)
        for i in range(size):
            r, c = q.popleft()
            for k in range(2):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    q.append((nr, nc))
                    bfs(nr, nc)
                    ans.append(sum_)


dr = [0, 1]
dc = [1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sum_ = 0
    bfs(0, 0)
    print(f"#{tc} {min(ans)}")
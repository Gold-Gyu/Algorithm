from collections import deque

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
maxV = 0
# 1 - 모양
# 2 ㅁ 모양
# 3 L 모양
# 4 번개 모양
# 5 ㅜ 모양

def bfs(i, j):
    global maxV

    q = deque()
    q.append((i, j))

    while q:
        size = len(q)
        for _ in range(size):

            r, c = q.popleft()

            # 1단계
            if 0 <= c+3 < m:
                ans = 0
                for k in range(4):
                    c1 = c + k
                    ans += field[r][c1]
                maxV = max(maxV, ans)
            if 0 <= r+3 < n:
                ans = 0
                for k in range(4):

                    r1 = r + k
                    ans += field[r1][c]
                maxV = max(maxV, ans)

            # 2단계
            if 0 <= c+1 < m and 0 <= r+1 < n:
                ans = 0
                ans += field[r][c]
                ans += field[r+1][c]
                ans += field[r][c+1]
                ans += field[r+1][c+1]
                maxV = max(maxV, ans)

            # 3 단계
            if 0 <= r+2 < n and 0 <= c-1 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r+1][c]
                ans += field[r+2][c]
                ans += field[r+2][c-1]
                # print("1번째", ans)
                maxV = max(maxV, ans)

            if 0 <= r + 2 < n and 0 <= c - 1 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r + 1][c]
                ans += field[r + 2][c]
                ans += field[r][c - 1]
                # print("2번째", ans)
                maxV = max(maxV, ans)

            if 0 <= c+1 < m and 0 <= r+2 < n:
                ans = 0
                ans += field[r][c]
                ans += field[r + 1][c]
                ans += field[r + 2][c]
                ans += field[r][c + 1]
                # print("3번째", ans)
                maxV = max(maxV, ans)

            if 0 <= c + 1 < m and 0 <= r + 2 < n:
                ans = 0
                ans += field[r][c]
                ans += field[r + 1][c]
                ans += field[r + 2][c]
                ans += field[r + 2][c + 1]
                # print("4번째", ans)
                maxV = max(maxV, ans)

            if 0 <= r-1 < n and 0 <= c+2 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r][c+1]
                ans += field[r][c+2]
                ans += field[r-1][c+2]
                # print("5번째", ans)
                maxV = max(maxV, ans)

            if 0 <= r+1 < n and 0 <= c + 2 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r+1][c]
                ans += field[r+1][c + 1]
                ans += field[r + 1][c + 2]
                # print("6번째", ans)
                maxV = max(maxV, ans)
            if 0 <= r + 2 < n and 0 <= c - 1 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r + 1][c]
                ans += field[r + 2][c]
                ans += field[r][c - 1]
                # print("7번째", ans)
                maxV = max(maxV, ans)

            if 0 <= r+1 < n and 0 <= c + 2 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r+1][c]
                ans += field[r][c + 1]
                ans += field[r][c + 2]
                # print("8번째", ans)
                maxV = max(maxV, ans)
            if 0 <= r + 1 < n and 0 <= c + 2 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r][c + 1]
                ans += field[r][c + 2]
                ans += field[r + 1][c + 2]
                # print("9번째", ans)
                maxV = max(maxV, ans)
            # 4 단계

            if 0 <= r+2 < n and 0 <= c + 1 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r + 1][c]
                ans += field[r + 1][c + 1]
                ans += field[r + 2][c + 1]
                # print("10번째", ans)
                maxV = max(maxV, ans)
            if 0 <= r + 2 < n and 0 <= c -1 < m:

                ans = 0
                ans += field[r][c]
                ans += field[r + 1][c]
                ans += field[r + 1][c - 1]
                ans += field[r + 2][c - 1]
                # print("11번째", ans)
                maxV = max(maxV, ans)

            if 0 <= r + 1 < n and 0 <= c + 2 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r][c + 1]
                ans += field[r + 1][c + 1]
                ans += field[r + 1][c + 2]
                # print("12번째", ans)
                maxV = max(maxV, ans)
            if 0 <= r + 1 < n and 0 <= c - 2 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r][c - 1]
                ans += field[r + 1][c - 1]
                ans += field[r + 1][c - 2]
                # print("13번째", ans)
                maxV = max(maxV, ans)

            # 5단계
            if 0 <= r + 1 < n and 0 <= c + 2 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r][c + 1]
                ans += field[r + 1][c + 1]
                ans += field[r][c + 2]
                # print("14번째", ans)
                maxV = max(maxV, ans)
            if 0 <= r + 2 < n and 0 <= c - 1 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r+1][c]
                ans += field[r + 1][c - 1]
                ans += field[r + 2][c]
                # print("15번째", ans)
                maxV = max(maxV, ans)
            if 0 <= r + 2 < n and 0 <= c + 1 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r+1][c]
                ans += field[r+1][c+1]
                ans += field[r+2][c]
                # print("16번째", ans)
                maxV = max(maxV, ans)
            if 0 <= r + 1 < n and 0 <= c + 1 < m and 0 <= c - 1 < m:
                ans = 0
                ans += field[r][c]
                ans += field[r+1][c]
                ans += field[r + 1][c - 1]
                ans += field[r+1][c + 1]
                # print("17번째", ans)
                maxV = max(maxV, ans)

for i in range(n):
    for j in range(m):
        bfs(i, j)
print(maxV)

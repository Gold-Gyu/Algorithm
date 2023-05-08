from collections import deque
def bfs(s):

    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        x = q.popleft()

        for node in adjL[x]:
            if v[node] == 0:
                v[node] = v[x] + 1
                q.append(node)


n, m = map(int ,input().split())

adjL = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    adjL[start].append(end)
    adjL[end].append(start)

v = [0] * (n+1)
cnt = 0
for i in range(1, n+1):
    if v[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)
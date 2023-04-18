from collections import deque

def bfs(p):
    visited = [0] * (N+1)
    cnt = 0
    q = deque()
    q.append(p)
    visited[p] = 1

    while q:
        t = q.popleft()
        for x in adj[t]:
            if visited[x] == 0:
                cnt += 1
                visited[x] = 1
                q.append(x)
    print(cnt)





N = int(input())    # 전체 노드의 개수
E = int(input())    # 전체 간선의 수
adj = [[] for _ in range(N+1)]

for i in range(E):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

bfs(1)
print(adj)

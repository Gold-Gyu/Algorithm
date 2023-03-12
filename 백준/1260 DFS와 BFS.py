def dfs(V):
    visited = [0] * (N + 1)
    stack = []
    ans = []
    v = V
    ans.append(v)
    visited[v] = 1

    while True:
        for w in adj[v]:
            if visited[w] == 0: # 방문하지 않았
                stack.append(v)
                ans.append(w)
                v = w
                # print(v)
                visited[w] = 1
                break # For w문 탈출
        else:
            if stack:
                v = stack.pop()
            else:
                print(*ans)
                break
    return

def bfs(adj, V, N):
    visited = [0] * (N+1)
    q = []
    ans2 = []
    v = V
    q.append(v)
    ans2.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)

        for i in adj[t]:
            if visited[i] == 0:
                q.append(i)
                ans2.append(i)
                visited[i] = visited[t] + 1
    print(*ans2)

N, M, V = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)
    adj[start].sort()
    adj[end].sort()

dfs(V)
bfs(adj, V, N)
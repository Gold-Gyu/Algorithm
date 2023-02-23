def dfs2(s, V):

    # 초기화부터 시작
    visited =[0] * (V+1)

    stack = []

    # 시작점에서
    i = s

    visited[i] = 1
    print(i)


    while True:

        for w in range(1, V+1):
            if adj[i][w] == 1 and visited[w] == 0:
                stack.append(i)

                i = w
                print(i)

                visited[w] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return


adj = [[0] * 8 for _ in range(8)]

for j in range(8):
    start, to = map(int, input().split())
    adj[start][to] = 1
    adj[to][start] = 1

print(adj)
dfs2(1, 7)
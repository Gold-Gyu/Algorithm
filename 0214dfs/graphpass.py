import sys
sys.stdin = open('sample_input (11).txt', 'r')

def dfs(s, V):

    # 초기화
    visited = [0] * (V + 1)
    stack = []
    # 현재 방문 정점 i
    i = s
    visited[i] = 1

    while True:

        for w in range(1, V + 1): #
            if adj[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[w] = 1
                break

        else:
            if stack:
                i = stack.pop()
                # 여기서 끝나고 다시 stack과 i 갱신해서 while문으로 간다.
            else:
                break
    if visited[G] == 1:
        return 1
    else:
        return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]

    for tc2 in range(E):
        start, to = map(int, input().split())
        adj[start][to] = 1

    S, G = map(int, input().split())
    print(f"#{tc} {dfs(S, V)}")




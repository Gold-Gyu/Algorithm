import sys
sys.stdin = open('input (19).txt', 'r')

# A : 0
# B : 99

def dfs(s, V):

    # 초기화
    visited = [0] * (V+1)
    stack = []

    # 현재방문
    i = s
    visited[i] = 1

    while True:
        for w in range(1, V+1):
            if adj[i][w] == 1 and visited[w] == 0:

                stack.append(i)
                i = w
                visited[i] = 1
                if visited[99] == 1:
                    return 1
                else:
                    break

        else:
            if stack:
                i = stack.pop()
            else:
                break
    return 0





for i in range(10):
    T, V = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[0] * 100 for _ in range(100)]
    s = 0
    v = 99

    for j in range(0, len(lst), 2):
        adj[lst[j]][lst[j+1]] = 1
    print(f"#{T} {dfs(s, v)}")
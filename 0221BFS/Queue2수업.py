# 연습문제 3
"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

"""
def bfs(v, N):  #v  #N
    # visited 생성
    visited = [0] * (N + 1)
    # 큐 생성
    q = [v]
    # 시작점 인큐
    visited[v] = 1
    # 시작점 인큐 표시

    while q:    # 큐가 비어있지 않으면
        t = q.pop(0)    # 디큐
        print(t, end = " ") # t에서 처리할 일
        # t에 인접이고 방문한ㄴ 적 없는 v
        for v in adjL[t]:
            if visited[v] == 0:
                # v인큐
                # v가 인큐 되었음을 표시
                q.append(v)
                visited[v] = visited[t] + 1
V, E = map(int, input().split())

arr = list(map(int, input().split()))

adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
    print(bfs(V, E))



# G : 그래프 정보(인접)
# v : 시작 정점의 번호
# n : 정점의 개수


def bfs(G, v, n):
    # 초기화
    # 방문배열 생성
    visited = [0] * (n+1)

    # 큐 생성
    q = []

    # 시작점 큐에 넣은 상태로 + 방문 도장
    q.append(v)
    visited[v] = 1

    # 반복 시작

    while q: # q가 비어있을 때까지 반복
        t = q.pop(0)    # 큐에 있는 가장먼저 들어왔던 원소 하나를 꺼내옴
        print(t)
        # 현재 정점 t에 연결된 모든 정점 i를 탐색
        for i in G[t]:
            # i 번 정점을 내가 방문한적이 없다면
            if not visited[i]:
                # 다음에 방문하기 위해 큐에 삽입
                q.append(i)
                # 방문처리
                visited[i] = visited[t] + 1


node = ["x", "A", "B", "C", "D", "E", "F", "G", "H", "I"]
"""
1. 그래프의 정보가 주어지는 어떻게 처리할 것인가?
정점의 개수 V
V = 9
간선의 수 E
E = 8

9 8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
4 9
"""

"""
7 8
1 2
1 3 
2 4 
2 5 
4 6 
5 6 
6 7 
3 7

"""


V, E = map(int, input().split())
G = [[] for _ in range(V+1)]

for i in range(E):  # 간선수 만큼 반복
    start, end = map(int, input().split())
    G[start].append(end)
    G[end].append(start)

print(G)
print(bfs(G, 1, V))
# 인접리스트
# G[A] - > [~~~~] 누구랑 연결되어있는지
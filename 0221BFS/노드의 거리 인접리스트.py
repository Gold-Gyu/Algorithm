import sys
sys.stdin = open('sample_input (4).txt', 'r')
from pprint import pprint

# G : 그래프 정보(인접)
# v : 시작 정점의 번호
# n : 정점의 개수


def bfs(G, S, V):
    # 초기화
    # 방문배열 생성
    visited = [0] * (V+1)

    # 큐 생성
    q = []

    # 시작점 큐에 넣은 상태로 + 방문 도장
    q.append(S)
    visited[S] = 1

    # 반복 시작
    while q:  # q가 비어있을 때까지 반복
        t = q.pop(0)  # 큐에 있는 가장먼저 들어왔던 원소 하나를 꺼내옴
        print(t)
        # 현재 정점 t에 연결된 모든 정점 i를 탐색
        for i in G[t]:
            # i 번 정점을 내가 방문한적이 없다면
            if not visited[i]:
                # 다음에 방문하기 위해 큐에 삽입
                q.append(i)
                # 방문처리
                visited[i] = visited[t] + 1



T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())


    print(bfs(G, S, V))
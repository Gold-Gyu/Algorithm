import sys
sys.stdin = open('sample_input (4).txt', 'r')
from pprint import pprint

# 방향성이 없는 그래프

"""
g 그래프 정보
s 시작노드
e 목표노드
v 노드개수
"""


def bfs(g, s, e, v):
    # 방문 배열
    visited = [0] * (v+1)
    # q 생성
    q = []
    # 노드 간의 거리
    distance = 0
    # 시작 노드 처리
    q.append(s)
    visited[s] = 1

    # q가 빌때까지 반복
    while q:
        t = q.pop(0)


        # 인접리스트를 통해서 현재 위치 t에서 갈 수 있는 노드를 모두 탐색
        for nt in g[t]:
            # 그 중에 내가 방문한 적이 없는 nt만 골라서 방문 처리
            if not visited[nt]:
                # 방문처리 + 거리계산
                visited[nt] = visited[t] + 1
                q.append(nt)
                # 다음 위치 nt가 목표 위치 e와 같다면
                if nt == e:
                    return visited[nt] - 1
    return 0

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())

    g = [[] for _ in range(v+1)]

    for i in range(e):
        left, right = map(int, input().split())
        g[left].append(right)
        g[right].append(left)

    # 시작 노드, 끝 노드
    sv, ev = map(int, input().split())
    print(f"#{tc} {bfs(g, sv, ev, v)}")
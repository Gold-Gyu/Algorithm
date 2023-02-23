import sys
sys.stdin = open('sample_input (4).txt', 'r')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]

    for i in range(E):  # 간선수 만큼 반복
        start, end = map(int, input().split())
        arr[start].append(end)
        arr[end].append(start)

    S, G = map(int, input().split())

    visited = [0] * (V + 1)

    # q생성
    q = []

    # 시작점
    v = S
    # 시작점 큐에 삽입
    # 방문배열 체크
    q.append(v)
    visited[v] = 1
    cnt = 0
    arrive = False
    while q:
        if visited[G] != 0:
            arrive = True
            break
        t = q.pop(0)
        for i in arr[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1

    if arrive == True:
        print(f"#{tc} {visited[G]-1}")
    else:
        print(f"#{tc} 0")
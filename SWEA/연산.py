import sys
sys.stdin = open("연산.txt", "r")

from collections import deque

T = int(input())


def bfs(N):

    q = deque() # 큐 생성하고
    visited = [0] * 1000001 # 방문함수 4가지 과정을 통해 나온 값 체크
    q.append(N) # 큐에 넣어주고


    while q:    # 큐가 빌때까지 반복
        size = len(q)
        for i in range(size): # 큐안에있는 갯수만큼 진행
            n = q.popleft() # 큐안에 있는 값을 꺼내서
            if n == M:  # M과 맞는지 확인
                return visited[M]  # 맞다면 cnt 출력

            # M과 같지 않다면
            for k in (n+1, n-1, n*2, n-10): # 4가지를 돌려보면서 수행
                if 0 <= k < 1000001 and visited[k] == 0:
                    # 계산한 값이 범위 안이고, 나온 값이 처음으로 나온 값이면
                    q.append(k)
                    visited[k] = visited[n] + 1
        # for i 가 끝까지 돌았다는 것은
        # bfs로 4가지 경우를 다돌렸기 때문에 연산 4가지 중 하나를 했다고 가정하기 떄문

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    # bfs(N)
    print(f"#{tc} {bfs(N)}")
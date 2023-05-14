"""

2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000

"""
from collections import deque

def startwalking(x, y, ex, ey):

    q = deque()
    v = [0] * n
    # 시작점을 큐에 넣어준다.
    q.append((x, y))

    while q:
        cj, ci = q.popleft()
        if abs(cj - ex) + abs(ci - ey) <= 1000:
            return "happy"  # 맥주를 마시면서 도착할 수 있다면 happy 출

        # 미방문 모든 편의점 좌표 : 범위 내인지 확인
        for i in range(n):
            if v[i] == 0: # 방문하지 않은 편의점이라면
                nj, ni = storelst[i]
                if abs(cj-nj) + abs(ci-ni) <= 1000:
                    q.append((nj, ni))
                    v[i] = 1
    return "sad"

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    homeX, homeY = map(int, input().split())
    storelst = []

    for store_num in range(n):
        storeX, storeY = map(int, input().split())
        storelst.append((storeX, storeY))
    festivalX, festivalY = map(int, input().split())

    ans = startwalking(homeX, homeY, festivalX, festivalY)
    print(ans)





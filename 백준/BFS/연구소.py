import sys; input = sys.stdin.readline
from collections import deque
import copy
"""
바이러스가 퍼지는걸 막아야한다.
바이러스는 상하좌우로 퍼지고
막아서 가장 많은 0을 지켜내는 값을 뽑는다.
벽 (1)은 3개만 세울 수 있다.
1. 먼저 벽을 세우고
2. 2를 상하좌우로 퍼져보고 1을 만나면 멈춘다.
3. 0의 개수를 세서
4. 가장 컸을 때를 출력한다.

나의 전략
1. 0인 지점에서 3개의 벽을 세웠을 모든 경우를 고려했을 때 0의 수가 가장 많이 보존된 값을 뽑는다.
2. 바이러스 퍼지는 것은 방문함수로 체크하고 꼭 초기화를 해준다.

모르겠는점
1. 0인 지점에서 벽 3개씩 모든 경우로 세워보는 방법
    즉, 조합을 2차행렬에서 어케 만들어야할지 모르겠음
    
조심해야할 부분
1. 벽세웠던거 다시 원상복귀해주기
2. 바이러스 퍼진거 다시 원상복귀해주

"""
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m

def wallmaker(idx):

    # 종료조건
    if idx == 3:
        spread()  # 2를 퍼트려라
        return

    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                lst[i][j] = 1
                wallmaker(idx + 1)
                lst[i][j] = 0


def spread(): # 2가 퍼지는
    global maxV
    zone = copy.deepcopy(lst)
    q = deque(virus)
    while q:
        size = len(q)
        for i in range(size):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid(nr, nc) and zone[nr][nc] == 0:
                    q.append((nr, nc))
                    zone[nr][nc] = 2
    cnt = 0
    for x in range(n):
        for y in range(m):
            if zone[x][y] == 0:
                cnt += 1
    maxV = max(maxV, cnt)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

v2 = [[0] * m for _ in range(n)]
maxV = 0

virus = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            virus.append((i, j))

wallmaker(0)
print(maxV)



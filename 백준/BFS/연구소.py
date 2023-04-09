"""
바이러스가 퍼지는걸 막아야한다.
바이러스는 상하좌우로 퍼지고
막아서 가장 많은 0을 지켜내는 값을 뽑는다.
벽 (1)은 3개만 세울 수 있다.
1. 먼저 벽을 세우고
2. 2를 상하좌우로 퍼져보고
3. 0의 개수를 세서
4. 가장 컸을 때를 출력한다.
"""


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:  # virus

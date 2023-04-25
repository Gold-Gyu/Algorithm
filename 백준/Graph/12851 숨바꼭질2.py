from collections import deque


def bfs(n):
    global minV
    global cnt
    global samething
    v = [0] * 100001
    q = deque()
    q.append(n)
    v[n] = 1

    while q:

        size = len(q)
        cnt += 1
        for _ in range(size):
            x = q.popleft()
            for nx in (x * 2, x + 1, x - 1):
                if 0 <= nx < 100001 and v[nx] == 0:
                    if nx == m:
                        samething += 1
                        minV = cnt

                    elif nx != m:
                        q.append(nx)
                        v[nx] = 1
        if minV == cnt:
            return


n, m = map(int, input().split())
minV = 99999
cnt = 0
samething = 0
if n == m:
    print(0)
    print(1)
else:
    bfs(n)
    print(minV)
    print(samething)

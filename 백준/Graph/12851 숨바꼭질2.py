from collections import deque


def bfs(n):

    global count
    flag = 0

    q = deque()
    q.append(n)
    v[n] = 1
    while q:

        size = len(q)

        for _ in range(size):
            x = q.popleft()
            if x == m:
                count += 1
            for nx in (x * 2, x + 1, x - 1):
                if 0 <= nx < 100001:

                    # 한번도 방문하지 않았거나 방문시간이 같은 경우
                   if v[nx] == 0 or v[nx] == v[x] + 1:
                        v[nx] = v[x] + 1
                        q.append(nx)


n, m = map(int, input().split())
v = [0] * 100001

count = 0
if n == m:
    print(0)
    print(1)
else:
    bfs(n)
    print(v[m]-1)
    print(count)

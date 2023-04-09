from collections import deque

# 5 17
def is_valid(n):
    return 0 <= n < 100001

def bfs(n, k):
    q = deque()
    q.append(n)
    v[n] = 1

    while q:
        size = len(q)
        for i in range(size):
            t = q.popleft()
            if t == k:
                return v[t] - 1
            for x in (t-1, t+1, t*2):
                if is_valid(x) and v[x] == 0:
                    q.append(x)
                    v[x] = v[t] + 1

n, k = map(int, input().split())
v = [0] * 100001

print(bfs(n, k))

# 경우의 수
# 1. 걷거나 +1, -1
# 2. 순간이동 하거나 *2,
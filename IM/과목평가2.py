def gogo():
    v = [[0] * N for _ in range(N)]
    (r, c) = 0
    stack = []
    stack.append(arr[r][c])
    v[r][c] = 1



T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = gogo()
    print(f"#{tc} {ans}")



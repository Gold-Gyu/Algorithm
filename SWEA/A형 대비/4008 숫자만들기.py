T = int(input())
def dfs(idx, sm, add, minus, mul, div):

    global mn, mx
    if idx == n:
        mx = max(mx, sm)
        mn = min(mn, sm)
        return

    if add > 0:
        dfs(idx+1, sm+lst[idx], add-1, minus, mul, div)
    if minus > 0:
        dfs(idx+1, sm-lst[idx], add, minus-1, mul, div)
    if mul > 0:
        dfs(idx+1, sm * lst[idx], add, minus, mul-1, div)
    if div > 0:
        dfs(idx+1, int(sm / lst[idx]), add, minus, mul, div-1)


for tc in range(1, T+1):
    n = int(input())
    add, minus, mul, div = map(int, input().split())
    lst = list(map(int, input().split()))
    mx, mn = int(-1e8), int(1e8)
    dfs(1, lst[0], add, minus, mul, div)
    print(f'#{tc} {mx-mn}')
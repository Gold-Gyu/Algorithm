n = int(input())

def dfs(idx, sm, add, sub, mul, div):
    global mn, mx
    # 가지치기
    # 결과값이나 중간값의 범위는 mn, mx = int(1e8), int(-1e8) 사이여야한다.
    if sm > int(1e9) or sm < int(-1e9):
        return

    # 종료조건
    if idx == n:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return

    # 2 하부호출 : 연산자 개수가 남아있는 경우만 호출 가능
    if add>0:
        dfs(idx+1, sm+arr[idx], add-1, sub, mul, div)
    if sub>0:
        dfs(idx+1, sm-arr[idx], add, sub-1, mul, div)
    if mul>0:
        dfs(idx+1, sm*arr[idx], add, sub, mul-1, div)
    if div>0:
        dfs(idx+1, int(sm/arr[idx]), add, sub, mul, div-1)

arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
mn, mx = int(1e9), int(-1e9)
dfs(1, arr[0], add, sub, mul, div)

print(mx, mn, sep="\n")
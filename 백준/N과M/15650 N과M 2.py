def dfs(n, lst):    # n 선택할 숫자
    if n>N: # 종료조건:n관련
        if len(lst) == M:   # M길이 수열 => 정답처리
            ans.append(lst)
        return

    # 선택하는 경우
    dfs(n+1, lst + [n])
    # 선택하지 않는 경우
    dfs(n+1, lst)


N, M = map(int, input().split())
ans = []
dfs(1, [])
for lst in ans:
    print(*lst)
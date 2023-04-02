def dfs(idx, s, selected):


    # 종료조건
    if idx == M:
        if len(selected) == M:
            print(*selected)
        return

    for j in range(s, N+1):
        # selected.append(i)
        dfs(idx+1, j, selected + [j])
        # dfs(idx+1, i, selected)
        # selected.pop()



N, M = map(int, input().split())
dfs(0, 1, [])
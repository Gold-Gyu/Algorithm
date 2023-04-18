def dfs(idx, selected):


    # 종료조건
    if idx == M:
        print(*selected)
        return

    for i in range(1, N+1):
        # if i not in selected:
        selected.append(i)
        # 포함하고
        dfs(idx+1, selected)
        selected.pop()



N, M = map(int, input().split())
dfs(0,[])
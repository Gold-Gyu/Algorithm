def dfs(idx, selected, sset):


    # 종료조건
    if idx == M:
        if len(selected) == M:
            sset.add(selected)
            print(*sset)
        return

    for i in range(1, N+1):
        # if i not in selected:

        # selected.append(i)
        dfs(idx+1, selected + [i], sset)
        dfs(idx+1, selected, sset)
        # selected.pop()



N, M = map(int, input().split())
sset = set()
dfs(0,[1], sset)
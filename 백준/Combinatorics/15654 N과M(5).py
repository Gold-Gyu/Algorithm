def dfs(idx, ans):

    # 종료조건

        # 정답처리
    if len(ans) == m:
        print(*ans)

        return

    if idx == n:
        return


    for i in lst:
        if i not in ans:
            ans.append(i)
            dfs(idx+1, ans)
            ans.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

dfs(0, [])
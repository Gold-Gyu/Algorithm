def backtracking(i):
    global cnt

    if sum(cc) == s and len(cc) > 0:
        cnt += 1

    for j in range(i, n):
        cc.append(lst[j])
        backtracking(i+1)
        cc.pop()


n, s = map(int, input().split())
lst = list(map(int, input().split()))
cc = []
cnt = 0
backtracking(0)
print(cnt)
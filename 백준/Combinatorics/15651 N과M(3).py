# n : 선택할 숫자의 개수
# 내가 1을 골랐다면 1보다 큰 수를 고르게 해야함
#

def dfs(n, s, lst): # n 내가 선택한 숫자의 개수 , s 시작점
    if n==M:    # M 개 선택완료
        ans.append(lst)
        return
    else:   # 선택해야한다면
        for j in range(s, N+1): # 시작점 s에서 N까지
            dfs(n+1, j+1, lst+[j])  # s부터 넣었기 때문에 s보다 큰 값을 넣어야 오름차순이 되므로 j+1을 한다



N, M = map(int, input().split())
ans = []
dfs(0, 1, [])
for lst in ans:
    print(*lst)
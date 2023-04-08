# ✨ 입력
def dfs(idx, s, lst):
    global minV
    # 종료조건
    if len(lst) == m:
        # 답 구하는 과정
        ans = []
        for i, j in lst:   # 치킨집의 좌표 하나씩 꺼내서
            for r, c in homes:
                s += abs(i-r) + abs(j-c)
                minV = min(minV, abs(i-r) + abs(j-c))
            ans.append(minV)
            print(ans)
        return sum(ans)

    # if idx == len(chickens):    # 다 돌았다면
    #     return
    for chicken in chickens:
        if chicken not in lst:
            lst.append(chicken)
            # 다음 치킨위치를 택한다.
            dfs(idx+1, lst)
            # 다음 치킨집의 좌표를 고르지않았을
            lst.pop()

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# ✨ 1
chickens = []
homes = []

minV = 100000

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

dfs(0, 0, [])

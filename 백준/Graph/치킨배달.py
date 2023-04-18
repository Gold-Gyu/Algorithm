"""
문제에서는 도시의 크기와 치킨집, 집의 위치 정보가 주어지며, 최대 M개의 치킨집을 선택하여 도시 내 모든 집으로부터 치킨 거리의 합이 최소가 되도록 배달해야 합니다.



"""


def dfs(idx, lst):
    global minV

    # 종료조건
    if len(lst) == m:   # m개의 치킨을 다 골랐다면

        ans = 0 # 각 집에서 치킨집까지 거리의 최소값들의 합
        # 집은 가장 가까운 치킨집으로 가야한다.

        # 정답처리
        for home in homes: # 집의 위치를 꺼내고
            home_cnt = 100000   # 최소값구하기
            for x in lst:   # 치킨집 중 m개를 고른 lst 하나하나 꺼내서

                # 하나의 집에서 치킨집까지의 거리 중 가장 작은 값을 구한다
                home_cnt = min(home_cnt, abs(home[0] - x[0]) + abs(home[1] - x[1]))
            ans += home_cnt # 가장 작은 치킨 거리 값을 더해준다

        # 가장 작은 치킨거리 값들의 합 : ans
        # 조합을 돌면서 총 가장 작은 치킨거리의 합을 가지고 있는 값을 출력한다.
        minV = min(minV, ans)
        return

    if idx == len(chickens): # 치킨지점을 모두 다 골라 봤다면
        return  # 리턴

    # 선택한다면
    dfs(idx+1, lst + [chickens[idx]])
    # 선택하지 않는다면
    dfs(idx+1, lst)

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chickens = []
homes = []
minV = 1000000


for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            homes.append((i, j))

dfs(0,[])
print(minV)
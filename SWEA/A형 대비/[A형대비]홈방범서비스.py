T = int(input())

cost = [(k*k + (k-1) * (k-1)) for k in range(1, 40)]

def solve():
    ans = 0
    # 1. 홈배열 생성
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append(arr[i][j])

    # 2. 모든 좌표를 순회하면서 distance배열 만들고, cnt
    for si in range(N):
        for sj in range(N):
            distance = [0] * 40
            # 집의 위치와 시작점 si, sj의 위치를 비교한다.
            for hi, hj in home: # 집 좌표를 하나씩 꺼내서
                t = abs(si-hi) + abs(sj-hj) + 1
                distance[t] += 1
            cnt = 0

            for k in range(1, 40):
                cnt += distance[k]
                if cost[k] <= cnt * k and ans < cnt:
                    ans = cnt
    return ans


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 # 집의 개수를 센다
    ans = solve()
    print(ans)
    # 일단 모든지점에서 완전탐색
    # 이후 한번 1이 있는 곳 시도해보기(집이 있는 곳을

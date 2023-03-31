T = int(input())

def dfs(idx, s, t): # s : 칼로리의 합, t = 맛점수의 합

    global maxV
    if s < l:
        if t < maxV:
            return

    # 종료조건
    if idx == n:
        if s <= l:
            maxV = max(maxV, t)
        return

    # 재귀호출
    # 선택했다면
    dfs(idx+1, s + cal[idx], t + taste[idx])
    # 선택하지 않았다면
    dfs(idx+1, s, t)


for tc in range(1, T+1):
    n, l = map(int, input().split())    # n : 재료, l : 칼로리

    taste = []
    cal = []

    for _ in range(n):
        A, B = map(int, input().split())
        taste.append(A)
        cal.append(B)
    print(taste)
    print(cal)
    maxV = 0
    dfs(0, 0, 0)
    # cal < l이면서 taste가 가장 큰 값
    print(f"#{tc} {maxV}")

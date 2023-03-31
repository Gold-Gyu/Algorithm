import sys
sys.stdin = open("[A형대비]수영장.txt", "r")


# 가능한 모든

def dfs(idx, s):
    global minV

    if minV <= s:
        return

    if idx > 12:

        minV = min(minV, s)
        return

    dfs(idx+1, s+day*lst[idx])
    dfs(idx + 1, s + mon)
    dfs(idx + 3, s + mon3)
    dfs(idx + 12, s + year)

T = int(input())

for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    minV = 365 * 3000
    dfs(1, 0)


    """
    # 규칙성 찾기
    s = [0] * 13
    for i in range(1, 13):
        가능한 방법중 i달까지의 최소비용
        s[i] = s[i-1] + day * lst[i]    # 일간권
        s[i] = min(s[i], s[i-1] + mon)  # 월간권
        if i >= 3:
           s[i] = min(s[i], s[i-3] + mon3)  # 분기권
        if i >= 12:
            s[i] = min(s[i], s[i-12] + year)  # 분기권
    ans = s[12]
    """

    print(f"#{tc} {minV}")
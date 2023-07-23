def dfs(n, plus):
    global ans
    # [1] 종료조건 : 가능한 n을 종료에 관련된 것으로 정의!
    if n >= N:
        # 정답처리
        ans = max(ans, plus)
        return

    # [2] 하부호출 : 화살표 개수만큼 표출
    # 2개일 경우 : 나란히 위 아래로 작성
    # 2개 초과 : for문으로 작성

    # 2-1 상담하는 경우
    if n + T[n] <= N: # 상담하는 경우(퇴사일 전에 완료 가능할)
        dfs(n+T[n], plus+P[n])

    # 2-2 상담하지 않는 경우( 항상 가능)
    dfs(n+1, plus)

N = int(input())
# 방법 1. 완전탐색 : 가능한 모든 경우를 탐색
# 방법 2. 그리디

T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())
ans = 0
dfs(0, 0)
print(ans)
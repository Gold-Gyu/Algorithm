N = int(input())
# "완료" 해야하는 상황이면 앞에서부터 진행하는 것보다 뒤에서부터 진행하는게 빠를 때가 많다.

T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

# dp 테이블 생성

dp = [0] * (N+1) # 초기값 한개 더 만들어줘야해서 N+1
for i in range(N-1, -1,-1): # 뒤에서 앞으로 실행
    if i+T[i] <= N: # 기간 내 상담완료가 가능하다면
        dp[i] = max(dp[i+1], dp[i+T[i]]+P[i])
    else:   # 기간내 상담 가능하지 않다면
        dp[i] = dp[i+1]

print(dp[0])

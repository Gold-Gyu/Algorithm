import sys
sys.stdin = open('sample_input (10).txt', 'r')



def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    return paper(n - 1) + paper(n - 2) * 2


T = int(input())

for tc in range(1, T+1):
    n = int(input()) // 10 # n = 1, 2, 3

    print(f"#{tc} {paper(n)}")

"""
DP 풀이
def dp(n):
    dp = [0] * 10001
    dp[1] = 1
    dp[2] = 3
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] * 2
    
    return dp(n)



"""
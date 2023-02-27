def fibo(n):

    if n < 2:
        return n

    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(5))

# 메모이제이션

n = 20
memo = [0] * 20
memo[1] = 1

def fibo1(n):
    # n 번째 항을 계산한적이 없고, n이 2 이상이라면
    # n 번째 항을 계산해야한다.
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

print(fibo1(7))


    # 계산한 적이 있으면 memo[n] 값을 그대로 사용하면 된다.
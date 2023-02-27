def fac(n):

    # 1. 종료 조건
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

print(fac(5))
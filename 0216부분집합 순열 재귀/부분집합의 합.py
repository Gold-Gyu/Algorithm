def f(i, k):
    if i == k:  # 하나의 부분집합 완성
        for j in range(k):
            if bit[j]:
                print(A[j], end = " ")
        print(bit)
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
A = [1, 2, 3]
n = len(A)
bit = [0] * n
f(0, n)

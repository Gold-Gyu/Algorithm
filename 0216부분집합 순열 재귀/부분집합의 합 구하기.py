def f(i, k):
    if i == k: # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]

        print(bit, s)
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(A)
answer = 10     # 내가 찾는값 ( 부분집합의 합이 10일 때)
bit = [0] * n
f(0, n)
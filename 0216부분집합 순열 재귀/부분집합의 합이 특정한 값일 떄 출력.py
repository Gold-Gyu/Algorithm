def f(i, k, answer):
    if i == k: # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]   # 부분집합의 합
        if s == answer: # 합이 answer와 같은 부분집합을 출력
            for j in range(k):
                if bit[j]:
                    print(A[j], end = " ")
            print()

    else:
        bit[i] = 1
        f(i+1, k, answer)
        bit[i] = 0
        f(i+1, k, answer)
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(A)
answer = 10     # 내가 찾는값 ( 부분집합의 합이 10일 때)
bit = [0] * n
f(0, n, answer)
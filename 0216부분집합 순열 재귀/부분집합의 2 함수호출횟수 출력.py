def f(i, k, s, t): # i 원소, k 집합의 크기, s (i-1까지)고려된 원소의 합, t 목표(찾고자하는 값)
    global cnt
    global fcnt
    fcnt += 1
    if i == k:
        if s == t:
            # for j in range(k):
            #     if bit[j]:
            #         print(A[j], end = " ")
            # print()                     # 부분집합의 합이 10일 수 있는 부분집합을 나타냄.
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1, k , s + A[i], t) # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함


cnt = 0
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(A)
key = 10 # 부분집합의 합이 10일 떄
answer = 100     # 내가 찾는값 ( 부분집합의 합이 10일 때)
bit = [0] * n
fcnt = 0 # 함수 호출 횟수
f(0, n, 0, key)
print(f"부분집합의 합이 {key}인 부분집합은 {cnt}개 입니다, 함수는 {fcnt} 호출됨")  # 합이 key인 부분집합의 수
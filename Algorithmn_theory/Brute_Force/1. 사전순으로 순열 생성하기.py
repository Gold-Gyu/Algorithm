def perm(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k): # 사용하지 않은 숫자를
            if used[j] == 0:    # used에서 순서대로 검색
                p[i] = A[j] # j 사용되지 않은 숫자를 넣는다
                used[j] = 1 # j번 자리 숫자를 사용했음을 표시
                perm(i+1, k)
                used[j] = 0  # j번 자리 숫자를 다른 자리에서 사용할 수 있도록 초기화

A = [1, 2, 3]
p = [0] * 3
used = [0] * 3
perm(0, 3)
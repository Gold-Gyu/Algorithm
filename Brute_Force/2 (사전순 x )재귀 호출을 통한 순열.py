def perm(i, k): # i는 값을 결정할 자리, k는 결정할 개수
    if i == k : # 모두 결정이 끝났으면
        print(*p)
    else: # 결정할게 남았으면
        for j in range(i, k): # 자신의 오른쪽 원소들과 교환
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]


p = [1,2,3]
perm(0, 3)
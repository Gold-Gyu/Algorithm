def nCr(n, r, s):
    if r == 0:
        print(comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)


n = 10
r = 3
comb = [0] * 3

A = [i for i in range(n)]
nCr(n, r, 0)
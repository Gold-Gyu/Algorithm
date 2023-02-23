import sys
sys.stdin = open('sample_input (6).txt', 'r')


T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())

    i = 0
    n = len(A)

    j = 0
    m = len(B)

    while i < n and j < m:
        if A[i] == B[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j == m:
        ans = i-1

    cnt = 0


    for i in range(ans, n):
        cnt += 1

    print(f"#{tc} {cnt}")


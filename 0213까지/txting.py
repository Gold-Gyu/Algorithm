import sys
sys.stdin = open('sample_input (6).txt', 'r')


T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())
    A = list(A)
    B = list(B)


    for i in A:
        for j in B:

        a = A.pop(B)
        print(a)

    # cnt = 0
    # if B
    # for i in range()
    # # for i in A:
    # if B in A:
    #     cnt += 1
    # print(cnt)
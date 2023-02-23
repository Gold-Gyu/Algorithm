import sys
sys.stdin = open('input_.txt', 'r')

lst = [2, 3, 5, 7, 11]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnts = [0] * len(lst)

    for i in range(len(lst)):
        while N % lst[i] == 0:
            cnts[i] += 1
            N = N // lst[i]

    print(f'#{tc}',*cnts)
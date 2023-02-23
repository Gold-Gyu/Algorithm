import sys

sys.stdin = open('s_input (1).txt', 'r')


T = int(input())


for tc in range(1, T + 1):

    D, A, B, F = map(int, input().split())
    ans = F * (D / (A+B))

    print(f'#{tc} {ans}')

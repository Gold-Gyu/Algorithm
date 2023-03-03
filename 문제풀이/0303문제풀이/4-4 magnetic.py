import sys
sys.stdin = open("input (3).txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    ans = 0
    for st in zip(*arr):
        ans += "".join(st).replace('0', '').count('12')

    print(f'#{test_case} {ans}')
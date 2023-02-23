import sys
sys.stdin = open('input (1).txt', 'r')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr2 = [[0] * (N+1) for _in range(N+2)]
    arr = [list(map(int, input().split())) for _ in range(M)]


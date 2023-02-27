import sys
sys.stdin = open('sample_input (16).txt', 'r')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    ans = ""
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                for h in range(M):
                    arr[i+k][-(i+k+1)]
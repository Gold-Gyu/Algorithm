import sys
sys.stdin = open('input (13).txt', 'r')
from pprint import pprint


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    # 기준점
    for i in range(N-M+1):
        for j in range(N-M+1):

            # 움직이는 방향
            sum_ = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    sum_ += arr[k][l]

            if maxV < sum_:
                maxV = sum_

    pprint(f"#{tc} {maxV}")




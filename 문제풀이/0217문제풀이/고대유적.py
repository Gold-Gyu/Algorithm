import sys
sys.stdin = open('input1 (1).txt', 'r')

# 점점커지는 당근의 개수의 가로세로버젼
# 사용하는 변수수의 위치와 초기값


def count(arr):
    maxV = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
    return maxV




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr)
    t = count(arr_t)
    if ans < t:
        ans = t

    print(f"#{tc} {ans}")
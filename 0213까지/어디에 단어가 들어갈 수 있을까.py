import sys
import pprint
sys.stdin = open('s_input (2).txt', 'r')

from pprint import pprint

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for i in lst:
            if i == 1:  # 단어를 넣을 수 있는 공백
                cnt += 1
            else:       # 칸없음
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    #arr와 arr_t로 각각 개수를 계싼
    arr_t = [[0] * (N+1) for _ in range(N+1)]
    print(arr_t)
    # arr_t = list(map(list, zip(*arr)))
    for i in range(N+1):
        for j in range(N+1):
            if i <= j:
                arr_t[i][j], arr_t[j][i] = arr[j][i], arr[i][j]
    pprint(arr_t)
            # print(list(arr_t))
    # 전치행렬
    print(count(arr))
    print(count(arr_t))
    ans = count(arr) + count(arr_t)

    print(f"#{tc} {ans}")
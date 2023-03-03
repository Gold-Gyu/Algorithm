import sys
sys.stdin = open("input (3).txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_t = list(zip(*arr))       # 전치행렬
    ans = 0 # 교착 개수
    for lst in arr_t:
        prev = 0
        for n in lst:
            if n != "0":   # n이 0이 아니면
                if n == "2" and prev == "1":
                    ans += 1
                prev = n    # 갱신
    print(f"#{tc} {ans}")
import sys
sys.stdin = open("input (19).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    k = -1
    count = 0
    for i in range(N):
        if i > N // 2:
            k -= 1
        else:
            k += 1
        for j in range(N//2 - k, N//2 + 1 + k):
            count += arr[i][j]
    print(f"#{tc} {count}")



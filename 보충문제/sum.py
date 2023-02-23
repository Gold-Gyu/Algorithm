import sys
sys.stdin = open('input (2).txt', 'r')


for tc in range(1, 11):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]


    # 가로의 합
    # 세로의 합
    # 좌 대각선 합
    # 우 대각선 합

    maxV = 0

    for x in range(100):
        cnt = 0
        for y in range(100):
            cnt += arr[x][y]
        if maxV < cnt:
            maxV = cnt

    for y in range(100):
        cnt = 0
        for x in range(100):
            cnt += arr[x][y]
        if maxV < cnt:
            maxV = cnt

    cnt = 0
    for x in range(100):
        cnt += arr[x][x]
    if maxV < cnt:
        maxV = cnt

    cnt = 0
    for x in range(99, -1 , -1):
        cnt += arr[x][x]
    if maxV < cnt:
        maxV = cnt


    print(f"#{tc} {maxV}")
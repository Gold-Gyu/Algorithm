import sys
sys.stdin = open('s_input (4).txt', 'r')

from pprint import  pprint


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    # 값을 저장한다
    a1 = [[0] * N for _ in range(N)]    # 90도
    a2 = [[0] * N for _ in range(N)]    # 180도
    a3 = [[0] * N for _ in range(N)]    # 270도

    # 회전각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-j][N-1-j]
            a3[i][j] = arr[j][N-1-i]
            # print(a1)
            # print(a2)
            # print(a3)
    print(f"#{tc}")
    for a, b, c in zip(a1, a2, a3):
        # print(a, b, c)
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')



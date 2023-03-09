

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    for i in (0, 3, 6):
        for j in (0, 3, 6):  # 3*3 격자
            lst = arr[i][j:j + 3] + arr[i + 1][j:j + 3] + arr[i + 2][j:j + 3]
            print(lst)

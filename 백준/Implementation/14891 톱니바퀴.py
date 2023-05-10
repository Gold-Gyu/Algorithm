from pprint import pprint

def bingbing(n, d):
    global direction

    if d == 1:
        direction = -1
    else:
        direction = 1
    lst = [0] * 8
    if direction == 1:
        # 우로 이동
        temp = arr[n - 1][7]
        for x in range(7):
            lst[x + 1] = arr[n - 1][x]
        lst[0] = temp
        arr[n - 1] = lst
    else:
        # 좌로 이
        temp = arr[n - 1][0]
        for x in range(7):
            lst[x] = arr[n - 1][x + 1]
        lst[7] = temp
        arr[n - 1] = lst

def bingbing2(n, direction):

    lst = [0] * 8
    if direction == 1:
        # 우로 이동

        temp = arr[n - 1][7]
        for x in range(7):
            lst[x + 1] = arr[n - 1][x]
        lst[0] = temp
        arr[n - 1] = lst
    else:
        temp = arr[n - 1][0]
        for x in range(7):
            lst[x] = arr[n - 1][x + 1]
        lst[7] = temp
        arr[n - 1] = lst


arr = [list(map(int, input())) for _ in range(4)]

k = int(input())

for _ in range(k):
    check1 =0
    check2 = 0
    check3 = 0
    good1 = 0
    good2 = 0
    n, direction = map(int, input().split())
    real_d = direction
    direction2 = direction
    if n == 1:
        if arr[n-1][2] != arr[n][-2]:
            check1 = 1
            if arr[n][2] != arr[n+1][-2]:
                check2 = 1
                if arr[n+1][2] != arr[n+2][-2]:
                    check3 = 1
        if check1:
            bingbing(n+1, direction)
        if check2:
            bingbing(n + 2, direction)
        if check3:
            bingbing(n + 3, direction)
    elif n == 2:
        if arr[n-2][2] != arr[n-1][-2]:
            good1 = 1
        if arr[n-1][2] != arr[n][-2]:
            check1 = 1
            if arr[n][2] != arr[n+1][-2]:
                check2 = 1
        if good1:
            bingbing(n - 1, direction)
            direction = real_d
        if check1:
            bingbing(n+1, direction)
        if check2:
            bingbing(n + 2, direction)

    elif n == 3:
        if arr[n-2][2] != arr[n-1][-2]:
            good1 = 1
            if arr[n-3][2] != arr[n-2][-2]:
                good2 = 1

        if arr[n-1][2] != arr[n][-2]:
            check1 = 1

        if good1:
            bingbing(n - 1, direction)
        if good2:
            bingbing(n - 2, direction)
            direction = real_d
        if check1:
            bingbing(n + 1, direction)

    elif n == 4:
        if arr[n-2][2] != arr[n-1][-2]:
            check1 = 1
            if arr[n-3][2] != arr[n-2][-2]:
                check2 = 1
                if arr[n-4][2] != arr[n-3][-2]:
                    check3 = 1
        if check1:
            bingbing(n-1, direction)
        if check2:
            bingbing(n - 2, direction)
        if check3:
            bingbing(n - 3, direction)
    bingbing2(n, real_d)

answer = 0
point = [1, 2, 4, 8]
for ans in range(4):
    if arr[ans][0] == 1:
        answer += point[ans]


print(answer)

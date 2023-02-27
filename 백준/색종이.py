from pprint import pprint

T = int(input())

arr = [[0] * 1001 for _ in range(1001)]

lst = [0] * (T+1)
for num in range(1, T+1):
    x, y, nx, ny = map(int, input().split())


    for i in range(x, x+nx):
        for j in range(y, y+ny):
            arr[i][j] = num

    cnt = 0
    for k in range(x, x+nx):
        for h in range(y, y+ny):
            if arr[k][h] == num:
                cnt += 1

    #             cnt += 1
    #             lst[num] += 1
    #         else:
    #             arr[i][j] = num
    #             lst[arr[i][j]] -= 1
    #             cnt += 1
    # print(cnt)
    # print(lst)




# for i in range(1, T+1):
#     cnt= 0
#     for k in range(1001):
#         for h in range(1001):
#             if arr[k][h] == i:
#                 cnt += 1
#     print(cnt)

# import sys
# sys.stdin = open('sample_input (4).txt', 'r')


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    for i in range(0, N, 2):
        max_idx = i
        for j in range(i+1, N):
            if arr[max_idx] < arr[j]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    for x in range(1, N, 2):

        min_idx = x
        for y in range(x+1, N):
            if arr[min_idx] > arr[y]:
                min_idx = y

        arr[x], arr[min_idx] = arr[min_idx], arr[x]


    print(f"#{tc}", *arr)

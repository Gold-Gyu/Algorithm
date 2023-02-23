import sys
sys.stdin = open('sample_input(1).txt', 'r')



T = int(input())

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(2)]

    cnts = [0] * len(arr[0])


    print(arr)


    for i in arr[1]:
        for j in range(len(cnts)):
            if i == arr[0][j]:
                cnts[j] += 1

    maxV = 0
    for p in cnts:
        if maxV < p:
            maxV = p

    print(f"#{tc} {maxV}")
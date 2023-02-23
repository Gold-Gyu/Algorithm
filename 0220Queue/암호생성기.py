import sys
sys.stdin = open('input (6).txt', 'r')


T = 10
for _ in range(1, T+1):
    tc = input()
    arr = list(map(int, input().split()))
    n = len(arr)
    Q = [0] * 100000
    rear = front = -1
    for i in arr:
        rear += 1
        Q[rear] = i


    k = 1
    while Q[rear] > 0:
        front += 1
        rear += 1
        Q[rear] = Q[front] - k
        if Q[rear] < 0:
            Q[rear] = 0
        k += 1
        if k == 6:
            k = 1
    front += 1
    rear += 1
    ans = Q[front:rear]

    print(f"#{tc}", *ans)








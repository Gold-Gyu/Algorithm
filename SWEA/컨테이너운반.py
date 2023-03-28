import sys
sys.stdin = open('컨테이너운반.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    weight = sorted(w, reverse=True)
    total = sorted(t, reverse=True)
    print(weight)
    print(total)

    cnt = 0

    a = len(total)
    b = len(weight)

    for i in range(a):
        for j in range(b):
            if weight[j] <= total[i] and weight[j] > 0:
                cnt += weight[j]
                weight[j] = 0
                break # for j

    print(f'#{tc} {cnt}')
import sys
sys.stdin = open('sample_in.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    stop = [0] * 1001 # 정류장

    for i in range(N):
        A = list(map(int, input().split()))

        for j in range(1, len(stop)+1):

            if A[0] == 1:
                if A[1] <= j <= A[2]:
                    stop[j] += 1

            elif A[0] == 2:
                if A[1] % 2 == 0:
                    if j % 2 == 0 and A[1] <= j <= A[2]:
                        stop[j] += 1

                else:
                    if j % 2 != 0 and A[1] <= j <= A[2]:
                        stop[j] += 1

            else:
                if A[1] % 2 == 0:
                    if j % 4 == 0 and A[1] <= j <= A[2]:
                        stop[j] += 1
                else:
                    if j % 3 == 0 and j % 10 != 0 and A[1] <= j <= A[2]:
                        stop[j] += 1
        maxi = 0
        for k in stop:
            if k > maxi:
                maxi = k

        for x in range(1, N+1):
            if maxi == x:
                ans = x


    print(f'#{tc} {ans}')

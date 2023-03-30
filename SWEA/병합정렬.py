import sys
sys.stdin = open("병합정렬.txt", "r")

def mergesort(left, right):
    global cnt

    if left == right - 1:
        return

    mid = (right + left) // 2

    if tmp[mid - 1] > tmp[right - 1]:
        cnt += 1

    mergesort(left, mid)
    mergesort(mid, right)

    l, r = left, mid
    if A[mid - 1] > A[right - 1]:
        cnt += 1

    for k in range(left, right):
        if r >= right:
            tmp[k] = A[l]
            l += 1

        elif l >= mid:
            tmp[k] = A[r]
            r += 1

        elif A[l] <= A[r]:
            tmp[k] = A[l]
            l += 1

        else:
            tmp[k] = A[r]
            r += 1

    for i in range(left, right):
        A[i] = tmp[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    tmp = [0] * len(A)
    cnt = 0
    mergesort(0, len(A))

    print(A)

    print(f'#{tc} {A[N//2]} {cnt}')
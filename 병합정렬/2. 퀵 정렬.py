def hoare(A, l, r):
    pivot = A[l]    # 맨 왼쪽 원소 기준
    i = l           # 피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = r           # 피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j: # 교차하지 않은 상태면
        while i <= j and A[i] <= pivot: # 피봇보다 크면 멈추고
            i += 1

        while i <= j and A[j] > pivot: # 피봇보다 작은걸 찾으러 왼쪽으로 이동
            j -= 1

        # while문들이 종료되면

        if i < j:   # 교차하지 않는 경우
            # j보다 오른쪽에 있는 애들은 피봇 보다 모두 큰 애들
            # i보다 왼쪽에 있는 애들은 피봇 보다 모두 작은 애들
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]
    return j


def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s-1)
        qsort((A, s+1, r))







T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N   # 이거 왜 만든거임? => 좌랑 우에서 정렬해서 가져올 임시 저장소

    qsort(arr, 0, N-1)   # 0부터 N-1구간까지 정렬을 해봐라
    print(*arr)
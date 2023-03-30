A = [5, 3, 4, 1, 2]
tmp = [0] * len(A) # 임시 저장소


def mergeSort(left, right):
    # 배열이 아닌 인덱스로 정렬

    # 종료조건
    # 원소가 하나가 남을 때 까지
    # 왼쪽 오른쪽이 같으면 원소가 1개임 why?
    if left == right:
        return

    # 분할
    # 가운데 지점
    mid = (left + right) // 2

    # 정복
    mergeSort(left, mid)    # 왼쪽부분
    mergeSort(mid+1, right) # 오른쪽 부분
    # 이 부분을 다 지났다는 거은

    # 결합
    # => 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
    # 작은 것을 먼저 맨 앞으로 큰 것을 맨 뒤로
    # 2개의 부분집합에서 맨 앞자리 비교해서 더 적은 값을 넣음

    # 왼쪽 부분, 오른쪽 부분의 시작 인덱스
    l, r = left, mid + 1

    # 임시 배열에 놓을 기준 위치 k
    # 지금 우리가 보고 있는 배열의 범위는 left ~ right
    for k in range(left, right+1):
        # 1. 왼쪽 부분만 남은 경우 : 왼쪽 배열 남은 것들 추가해주기
        if r > right:
            tmp[k] = A[l]
            l += 1
        # 2. 오른쪽 부분만 남은 경우 : 오른쪽 배열에 남은거 추가
        elif l > mid:
            tmp[k] = A[r]
            r += 1

        # 3. 둘다 남아 있다면
            # 3-1. 왼쪽이 작으면 왼쪽 것 추가
        elif A[l] < A[r]:
            tmp[k] = A[l]
            l += 1
            # 3-2. 오른쪽이 작으면 오른쪽 것 추가
        else:
            tmp[k] = A[r]
            r += 1

    # 복사
    for i in range(left, right + 1):    # 배열의 전체범위
        A[i] = tmp[i]

mergeSort(0, len(A)-1)
print(A)
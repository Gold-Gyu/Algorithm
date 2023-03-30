T = int(input())

"""
1
8
69 10 30 2 16 8 31 22



"""

# m : 정렬 대상 리스트
def mergeSort(m):
    # 종료
    if len(m) == 1:
        return m

    # 분할
    # 왼쪽 : left , 오른쪽 : right
    left = right = []
    # 가운데
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 정복
    left = mergeSort(left)
    right = mergeSort(right)

    print(f"mid : {mid}")
    print(f"left : {left}")
    print(f"right : {right}")

    # 다시 합치는 과정 : 병합    # 1조각까지 다 쪼갠다음에 병합과정 실시
    return merge(left, right)
    print(f"result : {result}")
    print("===================")

# 왼쪽과 오른쪽을 합쳐주는 함수
def merge(left, right):
    global cnt

    # 합병하기 전에
    # left의 제일끝, right의 제일 끝 비교
    if left[-1] > right[-1]:
        cnt += 1

    ln = len(left)
    rn = len(right)

    # 왼쪽에서 다음에 꺼낼 원소의 위치 : li
    # 오른쪽 : ri
    li = ri = 0

    # 결과 배열
    result = []

    # 왼쪽 또는 오른쪽에 원소가 하나라도 남아 있다면
    while li < ln or ri < rn:
        # 왼쪽 오른쪽 둘다 원소가 남아 있다면
        # 그중에 작은거부터 맨 앞에서 꺼내서 result에 추가
        if li < ln and ri < rn:
            if left[li] <= right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1
        # 왼쪽만 남아 있으면 왼쪽거 추가
        elif li < ln:
            result.append(left[li])
            li += 1
        # 오른쪽만 남아 있으면 오른쪽거 추가
        elif ri < rn:
            result.append(right[ri])
            ri += 1

    return result


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 왼쪽 부분의 제일 끝 원소가 오른쪽 부분의 제일 끝 원소보다 클때 개수 세기
    cnt = 0

    sorted_arr = mergeSort(arr)

    print(f"#{tc} {sorted_arr[N // 2]} {cnt}")
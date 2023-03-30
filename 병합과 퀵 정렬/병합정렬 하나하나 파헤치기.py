T = int(input())



"""
1
8
69 10 30 2 16 8 31 22



"""



# m : 정렬 대상 리스트


def mergesort(m):

    # 종료조건
    # 하나 남을때 까지
    if len(m) == 1: # 하나 남으면
        return m    # 자기 자신 리턴

    # ★분할
    # 왼쪽 : left, 오른쪽 : right
    left = right = []

    # 가운데
    mid = len(m) // 2
    left = m[:mid]  # 0 ~ mid-1 까지
    right = m[mid:] # mid ~ 끝까지

    # 정복 -> 다시 정렬
    left = mergesort(left)      # 왼쪽 정렬
    right = mergesort(right)    # 오른쪽 정렬

    print(f"mid : {mid}")
    print(f"left : {left}")
    print(f"right : {right}")


    # 다시 합치는 과정 : 병합    # 1조각까지 다 쪼갠다음에 병합과정 실시
    return merge(left, right)
    print(f"result : {result}")
    print("===================")
# 왼쪽과 오른쪽을 합쳐주는 함수
# 병합해주는 함수
def merge(left, right):
    global cnt

    # 합병전에
    # left의 제일 오른쪽, right의 제일오른쪽 비교
    if left[-1] > right[-1]:
        cnt += 1

    LN = len(left)
    RN = len(right)
    # 정렬할 대상이 왼쪽이 남아 있다면

    # 왼쪽에서 다음에 꺼낼 원소의 위치 : Li
    # 오른쪽에서 다음에 꺼낼 원소의 위치 : Ri
    Li = Ri = 0

    # 결과를 나타낼 결과배열
    result = []

    # 왼쪽 또는 오른쪽에 원소가 하나라도 남아 있다면
    while Li < LN or Ri < RN:
        # 왼쪽 오른쪽 둘다 원소가 남아있다면
        # 그중에 작은거부터 맨 앞에서 꺼내서 result에 추가
        if Li < LN and Ri < RN:
            if left[Li] <= right[Ri]:
                result.append(left[Li])
                Li += 1
            else:
                result.append(right[Ri])
                Ri += 1

        # 왼쪽만 남아있으면 왼쪽거 추가
        elif Li < LN:
            result.append(left[Li])
            Li += 1

        # 오른쪽만 남아 있으면 오른쪽거 추가
        elif Ri < RN:
            result.append(right[Ri])
            Ri += 1



for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    # 왼쪽 부분의 제일 끝 원소가 오른쪽 부분의 제일 끝 원소보다 클 때 개수 세기
    cnt = 0
    sorted_arr = mergesort(arr)
    print(sorted_arr)
    # print(f"#{tc} {sorted_arr[N//2]} {cnt}")
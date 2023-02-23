# 선택정렬
# 맨 앞자리부터 자리의 주인을 정해준다. (최솟값)
# i가 0일 때(인덱스가 0)일 때는 가장 작은수

def selection_sort(arr, n):
    # 1. 맨 앞자리부터 자리의 주인을 정해준다. 작은 숫자부터 순서대로
    for i in range(n-1):
        min_idx = i

        #2. i 의 뒤부터 비교를 시작하면서 최솟값 찾기
        for j in range(i+1, n): # 비교할때는 끝가지 해야하하기 때문에 n까지가 범위이다.
            # 제일 작은 숫자의 인덱스를 찾기
            if arr[min_idx] > arr[j]: #arr[j]는 최솟값
                min_idx = j # 제일작은 숫자의 인덱스를 찾음

        # 반복을 다 돌았으면 제일 작은 숫자를 현재자리 i로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [10, 25, 64, 22, 11]
n = len(arr)

selection_sort(arr, n)
print(arr)


"""

내림차순 정렬시


def selection_sort_asc(arr, n):
    # 1. 맨 앞자리부터 자리의 주인을 정해준다. 큰 숫자부터 순서대로
    for i in range(n-1):
        min_idx = i

        #2. i 의 뒤부터 비교를 시작하면서 최대값 찾기
        for j in range(i+1, n): # 비교할때는 끝가지 해야하하기 때문에 n까지가 범위이다.
            # 제일 큰 숫자의 인덱스를 찾기
            if arr[min_idx] < arr[j]: #arr[j]는 최솟값
                min_idx = j # 제일 큰 숫자의 인덱스를 찾음

        # 반복을 다 돌았으면 제일 큰 숫자를 현재자리 i로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [10, 25, 64, 22, 11]
n = len(arr)

selection_sort(arr, n)

"""

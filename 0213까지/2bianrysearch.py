def binary_search(arr, n, key):
    # 검색 범위 지정
    start = 0
    end = n - 1



    while start <= end:
    # 가운데 내가 찾는게 있다
    # 가운데를 찾는다.
    # 가운데 인덱스
        mid = (start + end) // 2  # 배열의 인덱스는 정수만 가능하기 때문에
        if arr[mid] == key:

            print(f"find")
            return mid

        elif arr[mid] > key:
            # 검색 범위를 재지정
            # 오른쪽은 더이 상 살펴볼 필요가 없다 => 뒤는 어차피 나보다 큰 수만 이씀
            # 검색의 끝 범위를 가운데로 가져온다.
            end = mid - 1 # 끝의 범위 인덱스를 수정

        else:
            # 검색 범위를 재지정
            # 왼쪽은 더 이상 ㅇ살펴볼 필요가 없음 => 나보다 작은 애들만 있음
            # 검색의 시작 범위를 가운데로 가져온다
            start = mid + 1

    return -1

# 반드시 정렬 필요
arr = [2, 3, 5, 7, 8, 16, 77]
n = len(arr)

print(binary_search(arr, n, 16))
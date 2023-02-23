import sys
sys.stdin = open('sample_input (4).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))
    # 기준위치(탐색을 시작할 위치)
    p = 0

    # 바꿀 대상 위치 (최대값과 최소값)
    idx = 0

    for i in range(10):
        # 정렬 시작
        # 기준 위치에서 최대값 또는 최솟값을 찾기 시작
        for j in range(i, N):
            if i % 2 == 0 and arr[j] > arr[idx]:
                # 최대값의 인덱스
                idx = j        # 최소값을 가지는 인덱스

            if i % 2 == 1 and arr[j] < arr[idx]:
                # 최소값의 인덱스
                idx = j

        arr[i], arr[idx] = arr[idx], arr[i]


    print(f"#{tc}", " ".join(map(str, arr[:10])))
    print(f"#{tc}", *arr[:10])
import sys
sys.stdin = open("퀵 정렬.txt", "r")



def partition(A, l, r):

    # 맨 왼쪽을 피봇으로 설정한다.
    p = A[l]

    i, j = l, r
    while i <= j:

        while i <= j and A[i] <= p:
            i += 1

        while i <= j and A[j] >= p:
            j -= 1

        if i < j:
            # i는 피봇보다 큰수를 찾고 j는 피봇보다 작은 수를 찾는데
            # j가 i보다 앞에 있다??
            # 잘된 것이기 때문에 서로 바꿔주기
            A[i], A[j] = A[j], A[i]

    # i와 j가 교차되었다는 말은
    # 피봇보다 작은 부분과 큰 부분으로 잘 나누었다는 의미
    # 피봇과 교차한 뒤의 j와 위치를 바꿔준다.

    A[l], A[j] = A[j], A[l]

    return j
    # 이제 피봇의 위치을 정해준다.



def quicksort(A, l, r):

    if l < r:   # 왼쪽 인덱스가 오른쪽 인덱스보다 커지면

        # 피봇의 위치 구하기(피봇보다 작은 원소들 경계점과 피봇보다 큰 원소들의 경계점 사이)
        s = partition(A, l, r)

        # 피봇의 위치를 구했으니
        # 피봇제외 왼쪽 정렬
        quicksort(A, l, s-1)
        quicksort(A, s+1, r)


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    A = list(map(int, input().split()))
    tmp = [0] * len(A)
    quicksort(A, 0, len(A)-1)
    print(f'#{tc} {A[n//2]}')

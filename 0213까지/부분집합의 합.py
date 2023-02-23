T = int(input())

arr = [i for i in range(1, 13)]
N = 12

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    # n = 부분집합 원소의 개수
    # k = 부분집합의 합

    answer = 0  # 위의 두 조건을 만족하는 부분집합의 개수
    # 원소의 개수가 n 이고 합이 k 인 부분집합의 개수

    # 부분집합의 총 개수만큼 반복 ==> 2^N
    for i in range(1 << N):

        # i번째 부분집합이 합이 k 이고 개수가 n인지 확인
        subset_sum = 0
        subset_count = 0
        # i번째 부분집합이 j번째 원소를 포함하는지 검사
        for j in range(N):
            if i & (1 << j):  # j 번째 인덱스의 원소를 부분집합에 포함하는지 검사

                subset_sum += arr[j]
                subset_count += 1

        print(f'합{subset_sum}')
        print(f'개수 {subset_count}')
        # n, k 검사
        if subset_count == n and subset_sum == k:
            answer += 1

    print(f"#{tc} {answer}")
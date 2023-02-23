
def counting_sort_asc(A, B, k):
    C = [0] * (k + 1)

    # 1의 원소의 등장 횟수를 센다.
    for i in range(len(A)):
        # A[i]의 등장횟수를 증가 시켜준다.
        # C[A[i]] = A[i]의 등장횟수
        C[A[i]] += 1
    print(C)
    # 2자리를 계산하는데... 내림차순
    for i in range(len(B)-2, -1, -1):
        # -2 인 이유는 마지막 자리는 그자리가 들어가기 때문에
        C[i] += C[i+1]
    print(C)

    for i in range(len(B) - 1, -1, -1):
        C[nums[i]] -= 1
        B[C[A[i]]] = A[i]

nums = [0, 4, 1, 3, 1, 2, 4, 1]
result_asc = [0] * 8
counting_sort_asc(nums, result_asc, max(nums))









    # 3 뒤에서부터 원소의 자리를 찾아주면된다.

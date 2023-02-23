# 합이 x보다 작은 부분집합만 구해야 한다면?
x = 6


numbers = [1, 2, 3, 4, 5]

# selected[i] == 1 => 내가 numbers 의 i 번째 원소를 부분집합에 포함 0
# selected[i] == 0 => 내가 numbers 의 i 번째 원소를 부분집합에 포함 x
selected = [0] * 5

n = len(numbers)
# 재귀 함수로 부분집합 구하기
# i 번째 원ㅅ를 부분집합에 포함할지 안할지 결정

def subset(i, subsum):  # subsum :
    # 0. 다른조건(최적화 조건)이 있는 경우
    if subsum >= x:  # 합 subsum이 목표값 x 보다 작은 경우
        return

    # 1. 재귀함수가 언제 끝날지(종료조건) 정해준다.
    # 종료조건
    if i == n:
        # n개의 원소에 대해 선택을 끝냈다.(고르던지 말든지)
        for j in range(n):
            if selected[j]: #
                print(numbers[j], end = " ")
        print()
        print("==========")
        return
    # 2. 재귀 호출

    # i 번째를 선택하고(부분집합에 포함 시킨다, selected[i]가 1) 다음 i + 1 번쨰 원소를 선택하러 가거나
    selected[i] = 1
    subset(i + 1, subsum + numbers[i])
    # i 번째를 선택하지 않고(부분집합에 포함 시키지 않음, selected[i]가 0) 다음 i + 1 번쨰 원소를 선택하러 가거나
    selected[i] = 0
    subset(i + 1, subsum)

subset(0, 0)
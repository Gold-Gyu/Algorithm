# 모든 부분집합을 구하는 방법


numbers = [1, 2, 3, 4, 5]

# selected[i] == 1 => 내가 numbers 의 i 번째 원소를 부분집합에 포함 0
# selected[i] == 0 => 내가 numbers 의 i 번째 원소를 부분집합에 포함 x
selected = [0] * 5

n = len(numbers)
# 재귀 함수로 부분집합 구하기
# i 번째 원소를 부분집합에 포함할지 안할지 결정

def subset(i):  # i는 시작 인덱스

    # selected 함수는 결국 n번째에 숫자를 선택하고 부분집합에 포함했는지 안했는지를 1과 0으로 표현하며 numbers의 인덱스로서 역할을 한다.
    # 1. 재귀함수가 언제 끝날지 정해준다.
    # 종료조건
    if i == n: # 원소 개수만큼 다 진행했을 때
        # n개의 원소에 대해 선택을 끝냈다.(고르던지 말든지)
        for j in range(n):
            if selected[j]: # selected함수의 j번째 원소가 1이라면 즉, numbers의 j번쨰 원소를 포함했다면
                print(numbers[j], end = " ")
        print()
        print("==========")
        return

    # 다 진행하지 않았다면
    # 2. 재귀 호출

    # i 번째를 선택하고(부분집합에 포함 시킨다, selected[i]가 1) 다음 i + 1 번쨰 원소를 선택하러 가거나
    selected[i] = 1
    subset(i + 1)
    # i 번째를 선택하지 않고(부분집합에 포함 시키지 않음, selected[i]가 0) 다음 i + 1 번쨰 원소를 선택하러 가거나
    selected[i] = 0
    subset(i + 1)

subset(0)
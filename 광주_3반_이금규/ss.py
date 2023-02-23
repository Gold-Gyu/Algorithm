


# i번째 원소의 자리를 바꿔가며 순열 생성
# 자리를 바꿀수 있는 경우의 수
def perm1(i):
    global cnt1
    # 1. 종료 조건
    if i == n:
        cnt1 += 1
        print(numbers)
        return

    # 2. 재귀 호출
    # 현재 위치 i에서 다른위치 j에 있는 숫자와 한번씩 다 바꿔보기
    # 이전에 i,j <==> j,i 처럼 바꾼거는 중복처리
    # 근데 위치를 바꾸지 않고 진행할수도 있다. i == j 이 경우는 위치를 바꾸지 않고
    # 다음 원소의 자리를 바꾸러 이동하는것이다.
    for j in range(i, n):
        # i 번째와 j 번째의 위치를 바꾸고 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
        # 다음 i+1 번째 원소의 자리를 바꾸러 간다.
        perm1(i + 1)
        # i 번째와 j 번째 위치를 되돌려 놓고 다음 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]


# cnt1 = 0
# perm1(0)
# print(cnt1)


# i번째의 자리를 누구로 할것인가 선택하는 방법
# i번째 자리가 누군지 기억해야 하므로 배열 필요
def perm2(i, selected):
    global cnt2

    # 1. 종료 조건
    if i == n:
        cnt2 += 1
        print(selected)

    # 2. 재귀 호출
    # 현재 위치 i에 누구를 놓을것인가 선택
    for j in range(n):
        # j번째 원소를 놓은적이 없다면 j 번째 원소를 i위치에 놓기
        if numbers[j] not in selected:
            # i위치는 j번째 원소가 선택되었다.
            selected[i] = numbers[j]
            # i위치의 주인을 정했으니 i+1 번째 위치의 주인을 정하러 갑니다.
            perm2(i + 1, selected)
            # i번째 위치의 j를 선택취소 하고 다음으로 이동
            selected[i] = 0


numbers = [1, 2, 3, 4, 5]
n = 5
cnt2 = 0
perm2(0, [0] * 5)


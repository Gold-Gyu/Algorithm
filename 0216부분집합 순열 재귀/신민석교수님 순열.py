numbers = [1, 2, 3, 4, 5]

n = 5

"""
예를 들어 자리가 5개가 있다면
첫번쨰 자리에서 자리를 교환하는 경우의 수
"""

# i번쨰 원소의 자리를 바꿔가며 순열 생성
# 자리를 바꿀 수 있는 경우의 수

def perm1(i):
    global cnt1
    # 1. 종료조건 : i 번쨰가 끝까지 왔을 떄
    if i == n:
        cnt1 += 1
        print(numbers)
        return

    # 2. 재귀호출
    # 현재 위치 i에서 다른위치 j에 있는 숫자와 한번씩 다 바꿔보기
    # 이전 i,j와 j,i가 바꾼 것은 같으므로 중복하지 않는다.(중복처리)
    # 하지만 위치를 바꾸지 않고 진행할 수 있음.
    # i == j인 경우 위치를 바꾸지 않고 다음 원소의 자리를 바꾸러 이동.
    for j in range(i, n):   # 중복처리를 위해 i에서부터 시작한다.
        # i 번쨰와 j 번쨰의 위치를 바꾸고 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
        # 다음 i + 1번째 원소의 자리를 바꾸러간다.
        perm1(i + 1)
        # i번쨰와 j번째 위치를 되돌려놓고 다음 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
cnt1 = 0
perm1(0)
print(cnt1)
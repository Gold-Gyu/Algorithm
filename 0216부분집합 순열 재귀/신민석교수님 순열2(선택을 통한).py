
# i 번쨰의 자리를 누구로 할 것인가 선택하는 방법
# i 번째 자리에 누가 있는지 기억해야 하므로 배열 필요
# 사전 순서로 볼 수 있다는 장점이 있다.
def perm2(i, selected):
    global cnt2

    #1. 종료조건
    if i == n:
        cnt2 += 1
        print(selected)

    # 재귀호출
    # 현재위치 i에 누굴 놓을 것인가
    for j in range(n):
        # j번째 원소를 놓은 적이 없다면 j번쨰 원소를 i 번쨰 위치에 넣기
        if numbers[j] not in selected:
            # i 위치는 j 번쨰 원소가 선택되었다.
            selected[i] = numbers[j]
            # i 위치를 정했으니 i + 1번째 위치를 정하러 간다
            perm2(i+1, selected)
            # i번째 위치의 j를 선택취소하고 다음으로 이동
            selected[i] = 0



numbers = [1, 2, 3, 4, 5]

n = len(numbers)

select_ = [0] * n

cnt2 = 0
perm2(0, select_)
print(cnt2)
import sys
sys.stdin = open('sample_input(1) (1).txt', 'r')
# 현재 i 번째 행에 대해서 j 번째 열을 골라서 합을 만들기

def backtracking(i, now_sum):
    global min_sum
    # 0. 가지치기
    # => 내가 지금까지 알고 있는 합보다 현재 합이 더 크면 이 밑으로 탐색할 이유가 없다.
    if now_sum > min_sum:
        return

    # 1. 종료 조건
    if i == n:
        if now_sum < min_sum:
            min_sum = now_sum
        return
    # 2. 재귀 호출
    # 0 ~ n - 1 번째 열 중에서 이전에 고른적이 없는 j 열 선택
    # i 번쨰 행에서 j 열에서 하나 고르면된다.
    for j in range(n):
        # 고른적이 없는지 확인
        if not selected[j]: # selected[j] 0이면
            selected[j] = 1
            # j 번째 열을 고르고 합을 구한 다음, 다음 행으로 진행
            backtracking(i+1, now_sum + board[i][j])
            # 다시 돌아와서 이번열을 건너뛰고 다음열로 진행하도록
            selected[j] = 0

    # j 열을 고르고 진행해보고(sum증가)
    # j 열을 고르지않고 진행하도록(sum 그대로)


T = int(input())

for tc in range(1, T+1):
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]
    selected = [0] * n      # 몇 번째 열을 선택했는지 확인
    min_sum = 100   # 모든수를 더해도 이 숫자를 넘을 수 없음
    backtracking(0, 0)

    print(f"#{tc} {min_sum}")
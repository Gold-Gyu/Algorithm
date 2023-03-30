import sys
sys.stdin = open("최소생산비용.txt", "r")

# 행마다 열을 선택
# row_num : 행번호(제품종류)
# selected : 이전에 고른 공장 중복 체크
# price : 가격의 합

def backtracking(row_num, selected, price):
    global minV

    # 가지치기
    # 어떤걸 보면 그 뒤에는 안봐도 될까???
    # 더 이상 가망이 없다면 ==
    if price >= minV:
        return

    # 종료 조건
    # 제품을 다 골랐다면 (행번호가 n)
    if row_num == n:
        minV = min(minV, price)
        return

    # 재귀 호출
    # 현재 row_num 행에서 고를 열번호 i를 선택
    for i in range(n):
        # i 열을 고를껀데, 이 열은 이전에 고른적이 없어야 한다.
        if i not in selected:
            selected.append(i)
            # 현재 행에서는 골랐음
            backtracking(row_num + 1, selected, price + factory[row_num][i])
            # 다른 i(열)를 고르러 가야하니까 초기화
            selected.pop()

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    factory = [list(map(int, input().split())) for _ in range(n)]

    minV = 15 * 100
    backtracking(0, [], 0)
    print(f"#{tc} {minV}")
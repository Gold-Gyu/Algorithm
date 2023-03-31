import sys
sys.stdin = open("전기버스2.txt", "r")

# 현재정류장의 위치 idx
# 충전횟수 cnt

# 충전횟수들 들고 다니는 이유
def backtracking(idx, cnt, selected):
    global minV

    # 가지치기
    # 현재까지 내가 충전한 횟수가 minV보다 크면 더이상 진행할 필요가 없다.
    if cnt >= minV:
        return

    # 종료조건
    if idx >= N - 1:
        minV = min(minV, cnt)
        print(selected, cnt)
        return

    # 재귀 호출
    # 현재 위치에서 갈 수 있는 곳 골라서 가기
    # 현재 위치 idx에서 갈 수 있는 곳 : idx + 1 ~ charge[idx]까지 갈 수 있음
    for i in range(1, charge[idx] + 1):
        selected.append(charge[idx])
        backtracking(idx + i, cnt + 1, selected)
        selected.pop()

T = int(input())

for tc in range(1, T+1):
    N, *charge = map(int, input().split())
    charge += [0]   # why?? 0을 넣은 것인가?
    minV = 100000   # 최소값
    backtracking(0, -1, [])
    print(f"#{tc} {minV}")

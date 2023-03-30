lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
cnt = 0

# 합이 10인 부분집합의 개수 구하기

# 현재위치 idx에 대하여 idx번째 원소를 선택 or 선택하지 않거나

def recur(idx, s, selected):  # s => 합 selectd => 내가 고른 것
    global cnt

    # 백트래킹 즉, 가지치기
    # 지금 idx번째 까지의 합이 10보다 크면 더 이상 탐색할 필요가 없음.
    if s > 10:
        return



    # 종료조건
    if idx == n:    # 모든 자리수를 다 골랐고
        if s == 10: # 합이 10이면
            cnt += 1
            print(selected) # 지금까지 내가 골랐던 것들
        return

    # 재귀 호출
    # idx 번째 원소를 선택 하거나
    selected.append(lst[idx])
    recur(idx+1, s+lst[idx], selected)
    # idx 번째 원소를 선택하지 않거나
    selected.pop()
    recur(idx+1, s, selected)

recur(0, 0, [])
print(cnt)
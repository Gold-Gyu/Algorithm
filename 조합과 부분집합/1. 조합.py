lst = [1, 2, 3, 4, 5]
N = 5
R = 3
# 총 원소는 5개고 3개를 골라야함

# N개 중에서 R개를 고르는 경우의 수

#

# 1. idx 번째 숫자를 고를지 고르지 않을지 결정
def comb(idx, r, selected):

    # 종료조건
    # 전체부분집합을 구할 때
    # 내가 n-1번째 원소를 고를지 말지 를 결정하고 나서가 종료조건임
    if idx == N:

        # r개 골랐을 때만 출력
        if r == R:
            print(selected)
        return
    # 재귀호출
    # 고르고 진행하던가
    selected.append(lst[idx])
    comb(idx+1, r + 1, selected)
    # 고르지 않고 진행하던가
    selected.pop()
    comb(idx + 1, r, selected)



# 2. R개를 고를떄까지 계속 선택
# 내가 idx번째 원소를 골랐다면, idx 이전에 있는 친구는 고려하지 않고
# 뒤에있는 것만 선택하겠다.

def comb2(idx, selected):

    # 종료조건
    if len(selected) == R: # 내가 고른것의 개수가 R이면
        print(selected)
        return

    # 재귀호출
    # 현재 위치 idx를 기준으로해서 다음 친구(i번쨰)를 고른다
    # i > = idx i번쨰 숫자를 하나 고르고 진행
    for i in range(idx, N):
        comb2(i+1, selected + [lst[i]])

comb(0, 0, [])
print("===========")
comb2(0, [])
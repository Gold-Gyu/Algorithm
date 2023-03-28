lst = [1,2,3,4,5]
n = 5

# idx가 0부터 n-1까지 돌려보기
# idx : idx번째 자리의 주인을 다른 누군가와 바꾸겠다.

def perm(idx):  # idx범위가 0 ~ 4

    # 종료조건
    if idx == n:
        print(lst)
        return

    #재귀 호출
    # 현재 idx 번째 숫자와 자리를 바꿀 i번째 숫자를 선택
    # idx = i가 같다면 자리를 바꾸지 않겠다는 의미
    # i를 정해주면 된다.

    # i를 정해줄 때 중복을 조심하기 위해서
    else:
        for i in range(idx, n):
            # 자리바꿔보고
            lst[idx], lst[i] = lst[i], lst[idx]
            perm(idx+1)
            # 다른 자리와 바꿔보기 위해 원상복귀
            lst[idx], lst[i] = lst[i], lst[idx]

N = 6   # 최대교환횟수
S = 6   # 길이
def perm2(cnt):

    # 종료조건
    # 교환횟수를 다 돌렸을 때 최대상금을 구하기

    if cnt == N:
        return

    # 재귀호출
    # 만약 교환횟수가 남았다면 카드를 바꾸면 된다.
    # 이 문제에서는 동일한 위치에서 중복 교환 허용하기 때문에
    # 자리 위치 2개(i, j)를 교환마다 새로 정해주어야한다.
    # 순차대로 하나씩 하는게 아니다.
    for i in range(S-1): # 뒤에 나랑 자리를 바꿀 한 개는 있어야한다
        for j in range(i+1, S):
            lst[i], lst[j] = lst[j], lst[i]
            perm2(cnt + 1)
            lst[i], lst[j] = lst[j], lst[i]


perm(0)
import sys
sys.stdin = open('sample_input.txt', 'r')

가위 = 1
바위 = 2
보 = 3


def winner(left, right):
    if cards[left] == 가위:
        if cards[right] == 바위:
            return right
        elif cards[right] == 보:
            return left
        else:
            return left if left < right else right
    elif cards[left] == 바위:
        if cards[right] == 보:
            return right
        elif cards[right] == 가위:
            return left
        else:
            return left if left < right else right
    elif cards[left] == 보:
        if cards[right] == 가위:
            return right
        elif cards[right] == 바위:
            return left
        else:
            return left if left < right else right


# i 가 왼쪽 , j 가 오른쪽
def tournament(i, j):
    # 1. 종료조건
    # 제일 작은 문제의 조건이 곧 종료 조건
    # 이때 해답을 구해서 return 해주면 된다.
    if i == j:
        return i

    # 2. 재귀 호출
    # 작은 문제의 해답들을 이용해서 큰 문제의해답을 구해 return
    left = tournament(i, (i + j) // 2)
    right = tournament((i + j) // 2 + 1, j)
    return winner(left, right)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    cards = list(map(int, input().split()))
    win = tournament(0, n - 1)
    print(f"#{tc} {win + 1}")
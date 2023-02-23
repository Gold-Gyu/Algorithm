import sys
sys.stdin = open('sample_input.txt', 'r')

def winner(L, R): # 가위바위보 작은

    if arr[L] == 1:
        if arr[R] == 2:
            return R
        elif arr[R] == 3:
            return L
        else:
            return L if L < R else R
    if arr[L] == 2:
        if arr[R] == 3:
            return R
        elif arr[R] == 1:
            return L
        else:
            return L if L < R else R
    if arr[L] == 3:
        if arr[R] == 1:
            return R
        elif arr[R] == 2:
            return L
        else:
            return L if L < R else R
# 토너먼트 진행
def tournament(i, j): #i부터 j까지

    # 1. 종료조건
    # 제일 작은 문제의 조건이 곧 종료조건
    # 이떄 해답을 구해서 return 해주면된다.
    if i == j: # 왼쪽사람과 오른쪽 사람
        return i

    # 2. 재귀호출
    left = tournament(i, mid) # 왼쪽에서 토너먼트 진행
    right = tournament(mid + 1, j)  # 오른쪽에서 토너먼트 진행
    return winner(left, right)





T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 1
    mid = (i + n) // 2  # 나누는 기준
    tournament(i, n)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('이금규 화이팅')
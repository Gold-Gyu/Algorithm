import sys
sys.stdin = open("최대상금.txt", 'r')


def perm2(cnt): # cnt는?
    global maxV

    # 종료조건
    # 교환횟수를 다 돌렸을 때 최대상금을 구하기
    if cnt == N:
        ans = int(''.join(S))
        if maxV < ans:
            maxV = ans
        return

    # 재귀호출
    # 만약 교환횟수가 남았다면 카드를 바꾸면 된다.
    # 이 문제에서는 동일한 위치에서 중복 교환 허용하기 때문에
    # 자리 위치 2개(i, j)를 교환마다 새로 정해주어야한다.
    # 순차대로 하나씩 하는게 아니다.
    for i in range(len(S) - 1):  # 뒤에 나랑 자리를 바꿀 한 개는 있어야한다
        for j in range(i + 1, len(S)):
            S[i], S[j] = S[j], S[i] # 자리를 바꾸고
            perm2(cnt + 1)
            S[i], S[j] = S[j], S[i] # 다시 돌아가서 다른 자리랑 바꾸기 위해 원상복귀


T = int(input())

for tc in range(1, T+1):
    S, N = input().split()
    S = list(S) # 리스트
    N = int(N)  # 교환횟수
    maxV = 0
    # 결국 순열의 경우의 수와 같다
    # 자리를 바꾸는 횟수가 순열의 길이보다 더 커봤자 어차피 중복
    if N > len(S):
        N = len(S)

    perm2(0)
    print(f"#{tc} {maxV}")

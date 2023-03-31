import sys
sys.stdin = open("장훈이의 높은 선반.txt", "r")

T = int(input())


def dfs(idx, s):

    global minV

    # 최소값 구할 때 항상 성공하는 가지치기
    # 이게 진짜 항상일까?

    # 종료조건
    if idx == N:

        if s >= B:    # b
            minV = min(minV, s-B)
        return

    # 재귀 호출
    # 포함했다면
    dfs(idx + 1, s+lst[idx])
    # 포함하지 않았다면
    dfs(idx + 1, s)


for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    minV = N * 10000
    dfs(0, 0)
    print(f"#{tc} {minV}")